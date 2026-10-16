"""Illustrative operational decision model for synthetic withdrawal-review events.

Only proposes analyst follow-up. NEVER recommends releasing funds, overriding holds,
disclosing restricted reasons or treating sample thresholds as Kraken policies.
"""
import json
from pathlib import Path
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
SAFE={"reviewing","action_required","completed"}
def instant(s):
    d=datetime.fromisoformat(s.replace("Z","+00:00"))
    if d.tzinfo is None:raise ValueError("timezone required")
    return d.astimezone(timezone.utc)
def decide(case):
    events=case["events"];src=[e for e in events if e["channel"]=="source"]
    if len(src)!=1:return {"route":"DATA_QUALITY","why":"No unique authoritative source event","owner":"Data Engineering","next":"Reconcile source event lineage"}
    s=src[0]
    if s["status"] not in SAFE:raise ValueError("Unknown approved state")
    anomalies=[];reference_risk=False
    for e in events:
        if e["status"] not in SAFE:raise ValueError("Unknown approved state")
        if e is s:continue
        if instant(e["at"])<instant(s["at"]):anomalies.append("EVENT_ORDER")
        if not e.get("approved",False):anomalies.append("UNAPPROVED_CONTENT")
        if e.get("support_reference") and not s.get("reference_allowed",False):reference_risk=True
        if e["status"]!=s["status"]:anomalies.append("CHANNEL_STATUS_MISMATCH")
    if reference_risk or "UNAPPROVED_CONTENT" in anomalies:
        return {"route":"POLICY_REVIEW","why":"Potential unapproved information surfaced","owner":"Risk / Compliance","next":"Contain disclosure and seek policy review; do not reveal review rationale"}
    if anomalies:
        return {"route":"DATA_QUALITY","why":"Conflicting or misordered channel information","owner":"Data / Product Operations","next":"Trace source timestamps, synchronization, and approved state mapping"}
    if case["hold_category"]=="scheduled":
        return {"route":"EXPECTED_HOLD","why":"Scheduled hold is a separate class from manual review","owner":"Support","next":"Confirm approved self-service guidance; no release recommendation"}
    if case["hold_category"]!="manual_review":raise ValueError("Unknown hold category")
    if case["repeat_contacts_7d"]>=2 and not case["approved_next_step_visible"]:
        return {"route":"COMMUNICATION_GAP","why":"Repeated contacts with no approved next-step visibility","owner":"Support / Product Operations","next":"Review approved customer-safe next-step messaging; preserve security constraints"}
    return {"route":"MONITOR","why":"No immediate discrepancy in available synthetic signals","owner":"Operations Analytics","next":"Track repeat contacts and exception trends; no automated action"}
def analyze(cases):
    ids=[x["case_id"] for x in cases]
    if len(ids)!=len(set(ids)):raise ValueError("Duplicate case IDs")
    result=[{"case_id":c["case_id"],**decide(c)} for c in cases]
    from collections import Counter
    return {"case_count":len(result),"route_counts":dict(sorted(Counter(r["route"] for r in result).items())),"decisions":result,"disclosure":"All events, flags and outcomes are fictional. Analyst triage only; no evidence of Kraken operational defects or measured impact."}
def main():
    cases=json.loads((ROOT/"data"/"decision_cases.json").read_text())
    out=analyze(cases)
    (ROOT/"data"/"decision_report.json").write_text(json.dumps(out,indent=2)+"\n")
    print(out["route_counts"])
if __name__=="__main__":main()
