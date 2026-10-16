# Evaluation of the October 16 public-status snapshot

This is a **reviewed subset** of a larger user-supplied ZIP proposal, not a claim that the full ZIP has been merged.

The supplied archive contains a standard-library feed parser, de-duplicated public update events, per-incident timings, tests and a more substantive landing-page summary. Its 18 included unit tests passed locally. A deprecation warning in the date parser was corrected locally, and the documentation's claim that the observed timestamp range was “about five days” was corrected: the event range is **September 30–October 16, 2026**, although events cluster October 11–16.

The [frozen report](../data/status_summary.json) from that archive covers **25 feed items and 88 posted updates** (10 incident items and 15 scheduled maintenance items). Of 6 keyword-matched money-movement incidents, 5 had a posted “Resolved” event; median interval from the first visible post to “Resolved” was **63 minutes**. The maximum gap between successive public updates in this subset was **315 minutes** for the USDT Ethereum withdrawal-delay item.

These are **public communication timestamps**, not observed incident starts, system downtime, personal withdrawal wait times, support response times or customer-level failures. Keyword matching is an illustrative categorization strategy and the sample is small. An update gap can simply mean no substantive change.

## Review outcome

Accepted as valuable: derive public communication metrics from real operational evidence rather than presenting injected synthetic rates as discoveries.

Pending for a complete merge: publish the archive's raw status-event CSV, the full RSS parser, fixture tests, report-generation validation, and any corresponding revised landing-page content together in one consistent version. Until then, the CSV-requiring quickcheck script reports a clear error if its input is absent.

Source: [Kraken official status history](https://status.kraken.com/history) · [status RSS](https://status.kraken.com/history.rss).

Data from the uploaded archive is treated as a frozen research snapshot, not live-confirmed external data.