# The Visibility Gap
**Independent Data Analytics & Operations case study · Felipe Mattos**

**[View the presentation](https://felipervm.github.io/kraken-withdrawal-visibility/site/)**

I studied how operational event data could help distinguish an expected withdrawal hold, contradictory customer-facing information, and a case requiring specialized review. The purpose is decision support, not criticism of Kraken's operations.

- **Verified public evidence:** Kraken's published *Crypto Withdrawal Delays* incident (July 29–31, 2026) spans **48h 33m**. This is **incident duration**, not customer delay. [Source & calculation](docs/PUBLIC-EVIDENCE.md).
- **Synthetic model:** six fictional review cases routed to data quality, communication, policy, expected-hold or monitoring workflows. No fabricated rates are claimed as discoveries.
- **Contribution demonstrated:** precise metric boundaries, event validation, prioritization, and clear ownership.
- **Run:** `python analysis/decision_engine.py && python -m unittest discover -s tests -v`
- **Deliverables:** [Executive decision brief](docs/DECISION-BRIEF.md) · [Public evidence notes](docs/PUBLIC-EVIDENCE.md) · [Python rules](analysis/decision_engine.py) · [Synthetic report](data/decision_report.json).
- **Career interest:** Junior Data Analyst / Data Operations · Canadian citizen · Canada-based remote roles.
- **Limitations:** Not affiliated with Kraken; no internal data, customer records, or actual incident-to-case linkage.

Further methodology, assumptions, archived public research and fixture details are in [docs/](docs/) and [analysis/](analysis/).

## Public feed analysis (reviewed archive)
A user-provided October 16 status-feed snapshot adds a useful real-data avenue: **25 feed items, 88 public updates**, with an illustrative median **63-minute interval between first posted update and resolution** among five resolved money-movement incidents. These are publication intervals, **not customer wait times**. [Review, scope and limitations](docs/FEED-REVIEW.md). The full parser and event-level input from the ZIP have not yet been merged.
