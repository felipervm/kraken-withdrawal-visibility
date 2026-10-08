# Research and evidence register

**Prepared:** October 8, 2026. **Author:** Felipe Mattos.

## Research question
When a withdrawal requires manual security review, are the customer's approved status and permitted next steps consistently communicated through the relevant touchpoints?

## Official documentation
1. [Kraken — Why is my account restricted?](https://support.kraken.com/articles/why-is-my-account-restricted): describes restrictions, security reasons, reviews, and email communication. In applicable cases, the support team may contact the customer within five business days; this is not a promise of resolution time.
2. [Kraken — Why is there a withdrawal hold on my account?](https://support.kraken.com/gb/articles/360000389606-why-is-there-a-withdrawal-hold-on-my-account-): distinguishes scheduled holds. Conditions depend on payment method, region and account circumstances; the page should be rechecked for up-to-date specifics.

## Qualitative reports — readable, underlying cases not corroborated
- https://www.reddit.com/r/KrakenSupport/comments/1wcdcez/withdrawal_on_hold/ — the author reports that chatbot guidance pointed to an existing ticket they could not locate, alongside missing email updates.
- https://www.reddit.com/r/KrakenSupport/comments/1wo0g35/withdrawal_on_hold_account_restricted_for_5_days/ — the author reports missing updates and difficulty reaching live chat. The author's interpretation of the timeframe is not verified policy.

Both posts were readable through web retrieval on October 8, 2026. Both contain responses from an account named krakensupport offering assistance. This verifies the presence of the reports, not their underlying chronology, authenticity, restriction category or resolution. Do not infer absolute post dates from relative dates on cached pages. No usernames or customer account identifiers are reproduced.

These are two previously selected reports, not a systematically collected sample. There is no denominator, frequency estimate, sentiment estimate or validated causal diagnosis.

## Important counter-evidence
The withdrawal-hold article (updated September 17, 2026; checked October 8) already documents a tooltip and chatbot lookup. The restriction article (updated July 8, 2026; checked October 8) describes email contact. This argues against claiming that Kraken has no visibility tools. The narrower hypothesis is **cross-channel continuity during eligible manual reviews**. Coverage of authenticated screens has not been tested.

## Competing explanations
- Restriction details may appropriately be withheld to prevent fraud and abuse.
- Different hold categories may not share the same release or communication conditions.
- Existing Kraken screens and chat channels may already display adequate permitted detail.
- Unusual customer complaints are overrepresented in public support communities.

## Proposed intervention
Only if a baseline audit demonstrates a meaningful gap: reconcile *approved* review status, relevant notification events, and permissible support references across channels. This study does not propose changing fraud rules, operational risk decisions, release promises, AML controls or investigation disclosure rules.

## Synthetic methods
The original demonstration contains 800 cases in three artificial categories: 412 scheduled holds, 302 manual reviews, 86 transient display scenarios. Exactly 40, 150 and 42 cases respectively have one or more **injected** communication QA exceptions, with overlap across four flags. Original row-level generator code was not provided, so its documented seed cannot independently establish regeneration. The original CSV is preserved as an immutable analytical input.

`analysis/generate_fixture.py` now generates an additional fixture with seed 42 and the same arbitrary category and exception counts. It does not reconstruct the original rows. Its code exposes all assumptions. `analysis/validate.py` validates both files and executes the supplied SQL in SQLite against the same rows. The notebook analyzes the original fixture using these shared checks.

Repeat-contact counts in both files are fabricated and deliberately associated with exception status. The resulting relationship is built into the simulation; it cannot support causation, savings or a Kraken impact claim. `transient_display` is an invented demonstration category, not a verified Kraken incident cause. The flags are pre-labeled inputs; the code validates and aggregates them rather than detecting actual stale messages from events.

## Verified original fixture outputs
| Category | Rows | Flagged rows | Injected rate | Simulated contacts, total |
| --- | ---: | ---: | ---: | ---: |
| scheduled_hold | 412 | 40 | 9.71% | 120 |
| manual_review | 302 | 150 | 49.67% | 136 |
| transient_display | 86 | 42 | 48.84% | 33 |

Total: 800 unique IDs, 232 flagged rows, zero union-flag mismatches. These rates describe fixture construction only.

## Internal evaluation
1. Define eligible case types and approved message taxonomy with Risk, Compliance and Support.
2. Map events and audit freshness and agreement across permitted communication channels.
3. Identify only the most bounded, actionable quality gap.
4. Test a small intervention against an appropriate baseline, if approved.
5. Primary metric: repeat support contacts per eligible manual review in seven days.
6. Guardrails: fraud/loss, inappropriate disclosure, complaints, inaccessible help-seeking and comprehension.
7. Stop or change course if the existing process is consistent or the security risk outweighs value.

## Operational definitions to agree internally
- Eligibility: one agreed manual-review category. Do not pool fixed holds or other restriction policies into its baseline.
- Primary outcome: total review-related repeat support contacts across accessible channels in the seven days after review entry, divided by all eligible reviews (including zero-contact cases). Define initial versus repeat contacts before analysis. Wait for a complete observation window and report unresolved cases separately.
- Proposed audit inputs: pseudonymous review ID, category, approved message version, channel, review-entry time, effective permitted-state time, message observation time, notification delivery result and related contact times. No confidential risk triggers are needed for this communication audit.
- Staleness: disagreement with the effective approved state beyond a team-approved delivery tolerance. Do not invent a universal timeout.
- Missing reference: an exception only if the eligible workflow requires a reference and it is safe to display. A zero flag is not proof of compliant messaging.
- Comparison: after a baseline audit, consider a concurrent randomized comparison for eligible cases if operationally appropriate. Select sample size and a minimum useful effect from real baseline variability, not this simulation. A before/after comparison alone is vulnerable to changes in case mix and volume.
- Guardrails: customer understanding, successful access to support, complaints, inappropriate disclosure and fraud/loss outcomes. A decline in contacts is not a win if access gets worse. Risk owners define monitoring horizon and stopping criteria; seven days may be too short for fraud outcomes.

## Business relevance and candidate signal
Possible value is reduced avoidable support effort and clearer customer understanding, conditional on an actual gap. No financial or retention effect has been measured. This project shows public-source judgment, data-contract checks, Python/SQL analysis, interface prototyping and evaluation design. It remains a portfolio demonstration, not production experience or a deployed Kraken system.

The strongest outreach framing is an invitation to critique a bounded hypothesis and discuss role fit. Avoid presenting the injected rates as discoveries or saying that a defect was found inside Kraken.

## Attribution and boundaries
No production data, personal information, confidential procedures, actual incident counts or causal savings claims. UI is a concept, not a depiction of the current Kraken experience.

## Event-derived demonstration (additional)
`analysis/event_consistency_demo.py` constructs four completely synthetic cases with an approved reference state and example app/email observations. It derives stale-state, cross-channel mismatch and unsafe-reference exceptions from timestamps, observed values and a hypothetical permission flag rather than pre-labeled QA flags. The tolerance is illustrative, not Kraken policy. This is a **demonstration of logic**, not analysis of production logs; real permissible fields and state semantics require approval from Risk, Compliance, Security and Support.
