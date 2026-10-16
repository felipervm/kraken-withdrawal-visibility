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