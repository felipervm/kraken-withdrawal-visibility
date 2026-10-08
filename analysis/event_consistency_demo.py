"""Event-derived consistency checks over entirely synthetic review communications.

This intentionally separate prototype goes beyond checking pre-labeled flags:
it constructs an event stream and derives the mismatches from the event data.
No Kraken account, support, fraud, or customer events are used.
"""
from collections import defaultdict
from datetime import datetime, timedelta, timezone

NOW = datetime(2026, 10, 8, 12, tzinfo=timezone.utc)
ALLOWED = {'reviewing', 'action_required', 'completed'}

def demo_events():
    """Four made-up cases: aligned, stale, inconsistent and unsafe reference."""
    return [
        {'case':'A', 'channel':'source', 'status':'reviewing', 'at':NOW, 'approved':True, 'reference_allowed':False},
        {'case':'A', 'channel':'app', 'status':'reviewing', 'at':NOW + timedelta(minutes=2), 'approved':True},
        {'case':'A', 'channel':'email', 'status':'reviewing', 'at':NOW + timedelta(minutes=4), 'approved':True},
        {'case':'B', 'channel':'source', 'status':'action_required', 'at':NOW, 'approved':True, 'reference_allowed':True},
        {'case':'B', 'channel':'app', 'status':'reviewing', 'at':NOW + timedelta(minutes=15), 'approved':True},
        {'case':'C', 'channel':'source', 'status':'reviewing', 'at':NOW, 'approved':True, 'reference_allowed':False},
        {'case':'C', 'channel':'app', 'status':'reviewing', 'at':NOW + timedelta(minutes=3), 'approved':True},
        {'case':'C', 'channel':'email', 'status':'completed', 'at':NOW + timedelta(minutes=4), 'approved':True},
        {'case':'D', 'channel':'source', 'status':'reviewing', 'at':NOW, 'approved':True, 'reference_allowed':False},
        {'case':'D', 'channel':'app', 'status':'reviewing', 'at':NOW + timedelta(minutes=2), 'approved':True, 'support_reference':'DEMO-123'},
    ]

def audit(events, permitted_delivery_minutes=10):
    """Only compares explicitly approved, non-sensitive synthetic state."""
    cases = defaultdict(list)
    for event in events:
        assert event['status'] in ALLOWED
        assert event.get('approved', False)
        cases[event['case']].append(event)
    issues=[]
    for case, group in sorted(cases.items()):
        sources=[event for event in group if event['channel']=='source']
        if len(sources)!=1:
            issues.append((case, 'missing_or_ambiguous_source'))
            continue
        source=sources[0]
        for item in group:
            if item is source: continue
            delta=(item['at']-source['at']).total_seconds()/60
            if item['status']!=source['status']:
                issues.append((case, 'cross_channel_mismatch' if delta<=permitted_delivery_minutes else 'stale_status'))
            if item.get('support_reference') and not source.get('reference_allowed',False):
                issues.append((case, 'reference_not_approved_for_display'))
    return issues

if __name__=='__main__':
    issues=audit(demo_events())
    print('Illustrative event-based issues:')
    for item in issues: print(*item,sep=': ')
    assert ('B','stale_status') in issues
    assert ('C','cross_channel_mismatch') in issues
    assert ('D','reference_not_approved_for_display') in issues
    assert not any(case=='A' for case,_ in issues)
    print('PASS: all expected demonstrations detected; control case clear')
