# The Visibility Gap

**[Open the study](https://felipervm.github.io/kraken-withdrawal-visibility/site/)**

Independent analytical case by Felipe Mattos. The central question: how can approved information and data quality help direct operational investigations without making unwarranted claims about Kraken's systems?

**Real public-data analysis:** A frozen snapshot of the [official status feed](https://status.kraken.com/history.rss) covers **25 status items and 88 published updates**. For five resolved incidents classified as money movement by keyword, the median interval from first observed publication to published resolution is **63 minutes**. **This measures status-update cadence, not withdrawal waiting time.**

**Reproducibility:** [event CSV](data/status_events.csv) · [standard-library parser](analysis/status_incidents.py) · [summary](data/status_summary.json) · [test suite](tests/test_status_snapshot.py) · [methodology](docs/PUBLIC-EVIDENCE.md).

**Synthetic demonstration:** Six made-up cases illustrate how an analyst would route discrepancies or questions to Support, Data Operations, Product Operations, Risk/Compliance or monitoring. They are not performance findings.

**Career objective:** Junior Data Analyst / Data Operations, Canadian citizen, interested in Canada-based remote roles.

**Run:** `python analysis/status_incidents.py && python analysis/decision_engine.py && python -m unittest discover -s tests -v`

Independent study; no internal Kraken access, customer records, or measured improvement. See [decision brief](docs/DECISION-BRIEF.md) for the proposed next steps.
