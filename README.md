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
- `analysis/validate.py` — CSV contracts and cross-checks using SQLite
- `analysis/generate_fixture.py` — deterministic additional fixture generator
- `data/generated_review_cases.csv` — additional generated fixture; does not reconstruct original rows
- `docs/RESEARCH.md` — evidence, competing explanations and proposed validation

## Run the analysis
From the repository root, these checks require only Python's standard library:
```bash
python analysis/validate.py
python analysis/generate_fixture.py
python analysis/validate.py data/generated_review_cases.csv
```

For the notebook:
```bash
python -m pip install pandas jupyter
jupyter notebook analysis/withdrawal_visibility.ipynb
```

The data deliberately include injected quality exceptions. All resulting metrics reflect a **simulation**; no real Kraken customer or operations data were used.

## Scope and limitations
Official Kraken help documentation distinguishes scheduled withdrawal holds from reviews and already describes hold-visibility tools. The two linked customer reports were readable on October 8, 2026; their underlying cases remain uncorroborated. The question is cross-channel continuity in eligible manual reviews. No prevalence, loss, release SLA or causal effect is claimed.

The original CSV has 800 unique IDs, 232 injected exception rows and zero union-flag mismatches. Its original generator was not supplied. The additional seeded generator exposes a new reproducible simulation with matching category totals; its rows and contact counts differ from the original. Flags are pre-labeled simulation inputs, not real event-based detection.

## Preview the page
```bash
python -m http.server 8765
```
Open `http://localhost:8765/site/`. GitHub Pages uses the root redirect to `site/`. The page has no build step or third-party asset dependencies.

Proposed evaluation: define permitted communication states with Risk/Compliance/Support, audit message consistency, and only test approved improvements. Primary metric: 7-day repeat support contacts per eligible review. Guardrails: fraud, customer understanding, support accessibility, complaints and improper disclosure.

© Felipe Mattos — Independent educational study, not affiliated with Kraken.
