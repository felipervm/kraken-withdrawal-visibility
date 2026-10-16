#!/usr/bin/env python3
"""Audit the frozen Kraken public-status feed; optionally merge fresh RSS events.
Measures publication cadence, never customer wait times, uptime or manual reviews.
"""
import argparse,csv,json,re,statistics,sys,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from email.utils import parsedate_to_datetime

ROOT=Path(__file__).resolve().parents[1]
FEED_URL="https://status.kraken.com/history.rss"
EVENTS=ROOT/"data/status_events.csv"
METRICS=ROOT/"data/status_incident_metrics.csv"
SUMMARY=ROOT/"data/status_summary.json"
FIELDS=["incident_id","title","status","timestamp_utc"]
INCIDENT={"investigating","identified","monitoring","resolved"}
MAINTENANCE={"scheduled","in progress","verifying","completed"}
MONEY=re.compile("withdraw|deposit|funding|transfer|gateway",re.I)
def dt(value):return datetime.fromisoformat(value.replace("Z","+00:00"))
def mins(x):return round(x.total_seconds()/60)
def median(x):return round(statistics.median(x)) if x else None
def strip_tags(s):return " ".join(re.sub(r"<[^>]+>","",s).split())
def parse_feed(xml):
    events=[]
    for item in ET.fromstring(xml).iter("item"):
        name=(item.findtext("title") or "").strip()
        iid=(item.findtext("guid") or item.findtext("link") or "").rstrip("/").rsplit("/",1)[-1]
        published=parsedate_to_datetime(item.findtext("pubDate")).astimezone(timezone.utc)
        desc=item.findtext("description") or ""
        for para in re.findall(r"<p>(.*?)</p>",desc,re.S):
            m=re.search(r"<small>(.*?)</small>.*?<strong>(.*?)</strong>",para,re.S)
            if not m:continue
            stamp=datetime.strptime(strip_tags(m.group(1))+" "+str(published.year),"%b %d, %H:%M UTC %Y").replace(tzinfo=timezone.utc)
            if stamp>published+timedelta(days=2):stamp=stamp.replace(year=stamp.year-1)
            events.append(dict(incident_id=iid,title=name,status=strip_tags(m.group(2)),timestamp_utc=stamp.strftime("%Y-%m-%dT%H:%M:%SZ")))
    return events
def load_events(path=EVENTS):
    with open(path,encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def merge_events(old,new):
    return sorted({(r["incident_id"],r["status"],r["timestamp_utc"]):r for r in old+new}.values(),key=lambda x:(x["timestamp_utc"],x["incident_id"],x["status"]))
def build_item_table(events):
    grouped=defaultdict(list)
    for e in events:grouped[e["incident_id"]].append(e)
    rows=[]
    for iid,items in grouped.items():
        items.sort(key=lambda x:x["timestamp_utc"])
        states={i["status"].lower() for i in items}
        kind="maintenance" if states&MAINTENANCE else "incident" if states&INCIDENT else "unknown"
        times=[dt(i["timestamp_utc"]) for i in items]
        by_state={}
        for t,e in zip(times,items):by_state.setdefault(e["status"].lower(),t)
        row=dict(incident_id=iid,title=items[0]["title"],kind=kind,money_movement=bool(MONEY.search(items[0]["title"])),first_post_utc=items[0]["timestamp_utc"],first_status=items[0]["status"],updates=len(items),resolved=("resolved" in states or "completed" in states),minutes_to_resolution="",minutes_to_second_post=mins(times[1]-times[0]) if len(times)>1 else "",longest_gap_minutes=max((mins(b-a) for a,b in zip(times,times[1:])),default=""),notice_hours="",has_in_progress_post="in progress" in states)
        if kind=="incident" and "resolved" in by_state:row["minutes_to_resolution"]=mins(by_state["resolved"]-times[0])
        if kind=="maintenance" and "scheduled" in by_state and "in progress" in by_state:row["notice_hours"]=round((by_state["in progress"]-by_state["scheduled"]).total_seconds()/3600,1)
        rows.append(row)
    return sorted(rows,key=lambda r:r["first_post_utc"])
def summarise(rows,events):
    incidents=[r for r in rows if r["kind"]=="incident"]
    maintenance=[r for r in rows if r["kind"]=="maintenance"]
    money=[r for r in incidents if r["money_movement"]]
    values=lambda ls,key:[r[key] for r in ls if r[key]!=""]
    def gap(ls):
        worst=max((r for r in ls if r["longest_gap_minutes"]!=""),key=lambda r:r["longest_gap_minutes"],default=None)
        return dict(minutes=worst["longest_gap_minutes"],incident=worst["title"],incident_id=worst["incident_id"]) if worst else None
    notice=[float(v) for v in values(maintenance,"notice_hours")]
    stamps=sorted(e["timestamp_utc"] for e in events)
    return dict(window_start_utc=stamps[0] if stamps else None,window_end_utc=stamps[-1] if stamps else None,feed_items=len(rows),events=len(events),incidents=len(incidents),maintenance_items=len(maintenance),money_movement_incidents=len(money),money_movement_incidents_open_at_snapshot=sum(not x["resolved"] for x in money),all_incidents=dict(resolved=len(values(incidents,"minutes_to_resolution")),median_minutes_to_resolution=median(values(incidents,"minutes_to_resolution")),first_post_already_past_investigating=sum(x["first_status"].lower()!="investigating" for x in incidents)),money_movement=dict(resolved=len(values(money,"minutes_to_resolution")),median_minutes_to_resolution=median(values(money,"minutes_to_resolution")),median_minutes_to_second_post=median(values(money,"minutes_to_second_post"))),longest_gap_all_incidents=gap(incidents),longest_gap_money_movement=gap(money),maintenance=dict(with_notice_data=len(notice),notice_under_1h=sum(x<1 for x in notice),notice_24h_or_more=sum(x>=24 for x in notice),median_notice_hours=round(statistics.median(notice),1) if notice else None,without_in_progress_post=sum(not x["has_in_progress_post"] for x in maintenance)),method_note="Timestamps are status-page publication times, not problem start times or customer waiting times.")
def write_outputs(rows,summary):
    with METRICS.open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");writer.writeheader();writer.writerows(rows)
    SUMMARY.write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fetch",action="store_true")
    p.add_argument("--feed-file")
    args=p.parse_args(argv)
    events=load_events()
    if args.fetch or args.feed_file:
        try:
            if args.fetch:
                req=urllib.request.Request(FEED_URL,headers={"User-Agent":"independent-visibility-research/1.0"})
                with urllib.request.urlopen(req,timeout=20) as res:xml=res.read().decode("utf-8")
            else:xml=Path(args.feed_file).read_text(encoding="utf-8")
            events=merge_events(events,parse_feed(xml))
        except (OSError,ValueError,ET.ParseError) as e:
            print("Public feed retrieval failed:",e,file=sys.stderr);return 1
    if not events:raise ValueError("No public events in CSV")
    if args.fetch or args.feed_file:
        with EVENTS.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator="\n");w.writeheader();w.writerows(events)
    write_outputs(build_item_table(events),summarise(build_item_table(events),events))
    print("Public feed:",len(events),"updates;",len(build_item_table(events)),"items")
    return 0
if __name__=="__main__":sys.exit(main())
