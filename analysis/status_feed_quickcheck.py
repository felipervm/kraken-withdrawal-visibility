"""Reproducible, read-only analysis of a public Kraken status-page event CSV.

For a frozen 2026-10-16 snapshot see data/status_summary.json.
Event timestamps are publication timestamps, NOT user waiting times.
This script never changes withdrawal settings or interacts with accounts.
"""
import csv, json, statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def minutes(a,b):
 return round((datetime.fromisoformat(b.replace("Z","+00:00"))-
               datetime.fromisoformat(a.replace("Z","+00:00"))).total_seconds()/60)
def summarize(rows):
 groups=defaultdict(list)
 for r in rows:groups[r["incident_id"]].append(r)
 totals=[];money=[]
 for entries in groups.values():
  entries.sort(key=lambda x:x["timestamp_utc"])
  if not any(x["status"].lower() in ("investigating","identified","monitoring","resolved") for x in entries):continue
  resolution=next((x for x in entries if x["status"].lower()=="resolved"),None)
  if not resolution:continue
  dur=minutes(entries[0]["timestamp_utc"],resolution["timestamp_utc"])
  totals.append(dur)
  if any(v in entries[0]["title"].lower() for v in ("withdraw","deposit","funding","transfer","gateway")):money.append(dur)
 return {"resolved_incidents":len(totals),"median_first_public_post_to_resolution_min":round(statistics.median(totals)) if totals else None,"money_movement_resolved":len(money),"money_movement_median_min":round(statistics.median(money)) if money else None,"scope":"public communication timestamps, not customer-level withdrawal duration"}
def main():
 path=ROOT/"data/status_events.csv"
 if not path.exists():raise SystemExit("Supply the public feed snapshot as data/status_events.csv (see docs/FEED-REVIEW.md).")
 with path.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
 print(json.dumps(summarize(rows),indent=2))
if __name__=="__main__":main()
