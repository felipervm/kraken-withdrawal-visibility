# Public status-page communication cadence — 2026-10-16 snapshot

**Source:** [Kraken official status history RSS](https://status.kraken.com/history.rss). A frozen subset of **88 public update events across 25 items** was supplied in the user-uploaded ZIP and checked with the parser and local unit tests.

## Metrics from posted public updates

| Measure | Value |
| --- | ---: |
| Feed items | 25 (10 incidents, 15 maintenance windows) |
| Public posts | 88 |
| Money-movement incidents (keyword match) | 6 (5 resolved, 1 unresolved) |
| Median first visible post → “Resolved” (resolved money-movement incidents) | **63 minutes** (n=5) |
| Median first visible post → “Resolved” (all resolved incidents) | **130 minutes** (n=8) |
| Median first → second posted update (money-movement incidents) | **31 minutes** |
| Largest update gap (money-movement incidents) | **315 minutes**, USDT withdrawal delays on Ethereum |
| Maintenance items with scheduled-to-in-progress interval below 1 hour | 7 of 14 |

**Caution:** These are gaps between public *publication timestamps*. They are not customer withdrawal delays, incident start-to-recovery times, support response times, platform availability, or indicators of wrongdoing. A long gap may indicate no change. Snapshot covers posts ranging from September 30 to October 16; concentration is October 11–16 and sample is not representative.

## Reproduction

```bash
python analysis/status_incidents.py
python -m unittest discover -s tests -v
```

Inputs: [frozen public events](../data/status_events.csv). Output: [summary](../data/status_summary.json) and generated `data/status_incident_metrics.csv`.

Optional updates: `python analysis/status_incidents.py --fetch` downloads and merges new RSS updates; `--feed-file path.xml` ingests a saved RSS export. Network fetching is **opt-in** and is not run in CI.

The older July 29–31 incident example remains a distinct historical reference rather than part of this snapshot. For analyst application, a next step would be a permitted comparison of status timelines and customer-safe messages using authorized internal datasets.
