# The Visibility Gap — Kraken withdrawal-review communications

Independent proof-of-work by **Felipe Mattos**. This is a job-interest portfolio study, **not a consulting or service pitch**. Not affiliated with Kraken.

## Business question
Can approved status and next-step communication across manual withdrawal reviews become more consistent without weakening security?

## Live study
https://felipervm.github.io/kraken-withdrawal-visibility/

## Deliverables
- `site/index.html` — visual research narrative and conceptual communication design
- `data/synthetic_review_cases.csv` — 800 seeded, entirely synthetic test cases
- `data/data_dictionary.json` — schema and simulation disclosure
- `analysis/withdrawal_visibility.ipynb` — reproducible quality checks and analysis
- `analysis/qa_queries.sql` — portable SQL examples
- `docs/RESEARCH.md` — evidence, competing explanations and proposed validation

## Run the analysis
```bash
python -m pip install pandas jupyter
jupyter notebook analysis/withdrawal_visibility.ipynb
```

The data deliberately include injected quality exceptions. All resulting metrics reflect a **simulation**; no real Kraken customer or operations data were used.

## Scope and limitations
Official Kraken help documentation distinguishes scheduled withdrawal holds from security reviews. Customer discussions are *exploratory leads*; the two discussion URLs cited in the site could not be independently reopened during the initial research. No prevalence, loss, SLA, or causal effect is claimed.

Proposed evaluation: define permitted communication states with Risk/Compliance/Support, audit message consistency, and only test approved improvements. Primary metric: 7-day repeat support contacts per eligible review. Guardrails: fraud, customer understanding, support accessibility, complaints and improper disclosure.

© Felipe Mattos — Independent educational study, not affiliated with Kraken.
