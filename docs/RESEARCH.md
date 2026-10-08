# Research and evidence register

**Prepared:** October 8, 2026. **Author:** Felipe Mattos.

## Research question
When a withdrawal requires manual security review, are the customer's approved status and permitted next steps consistently communicated through the relevant touchpoints?

## Official documentation
1. [Kraken — Why is my account restricted?](https://support.kraken.com/articles/why-is-my-account-restricted): describes restrictions, security reasons, reviews, and email communication. In applicable cases, the support team may contact the customer within five business days; this is not a promise of resolution time.
2. [Kraken — Why is there a withdrawal hold on my account?](https://support.kraken.com/gb/articles/360000389606-why-is-there-a-withdrawal-hold-on-my-account-): distinguishes scheduled holds. Conditions depend on payment method, region and account circumstances; the page should be rechecked for up-to-date specifics.

## Qualitative leads — not independently confirmed
- https://www.reddit.com/r/KrakenSupport/comments/1wcdcez/withdrawal_on_hold/ — previously surfaced question about visibility of status and a support reference.
- https://www.reddit.com/r/KrakenSupport/comments/1wo0g35/withdrawal_on_hold_account_restricted_for_5_days/ — previously surfaced account of difficulty obtaining a review update.

Direct reopening was unsuccessful during the initial research. These URLs are **leads for further validation**, not independent proof of an internal fault. The site does not quote unverified posts, assert prevalence or identify individuals.

## Competing explanations
- Restriction details may appropriately be withheld to prevent fraud and abuse.
- Different hold categories may not share the same release or communication conditions.
- Existing Kraken screens and chat channels may already display adequate permitted detail.
- Unusual customer complaints are overrepresented in public support communities.

## Proposed intervention
Only if a baseline audit demonstrates a meaningful gap: reconcile *approved* review status, relevant notification events, and permissible support references across channels. This study does not propose changing fraud rules, operational risk decisions, release promises, AML controls or investigation disclosure rules.

## Synthetic methods
The demonstration contains 800 cases in three artificial categories: 412 scheduled holds, 302 manual reviews, 86 transient display issues. A fixed pseudorandom seed of 42 distributes records. Exactly 40, 150 and 42 cases respectively have one or more **injected** communication QA exceptions, with overlap across four exception flags. Repeat-contact counts are also simulated and deliberately correlated with exception status. These are invented test inputs, **not Kraken estimates**.

## Internal evaluation
1. Define eligible case types and approved message taxonomy with Risk, Compliance and Support.
2. Map events and audit freshness and agreement across permitted communication channels.
3. Identify only the most bounded, actionable quality gap.
4. Test a small intervention against an appropriate baseline, if approved.
5. Primary metric: repeat support contacts per eligible manual review in seven days.
6. Guardrails: fraud/loss, inappropriate disclosure, complaints, inaccessible help-seeking and comprehension.
7. Stop or change course if the existing process is consistent or the security risk outweighs value.

## Attribution and boundaries
No production data, personal information, confidential procedures, actual incident counts or causal savings claims. UI is a concept, not a depiction of the current Kraken experience.
