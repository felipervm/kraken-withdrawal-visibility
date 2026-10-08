-- Load data/synthetic_review_cases.csv into synthetic_review_cases.
-- These are fabricated demonstration data, not measurements from Kraken.
SELECT review_type,
       COUNT(*) AS cases,
       SUM(communication_exception) AS flagged_cases,
       ROUND(100.0 * SUM(communication_exception) / NULLIF(COUNT(*),0),2) AS flagged_percent,
       ROUND(AVG(repeat_contacts_7d * 1.0),3) AS avg_repeat_contacts
FROM synthetic_review_cases
GROUP BY review_type ORDER BY review_type;

-- Expect zero rows if union flag is consistent with the four injected flags.
SELECT case_id FROM synthetic_review_cases
WHERE communication_exception <> CASE WHEN
  status_stale=1 OR missing_support_reference=1 OR
  cross_channel_mismatch=1 OR missed_permitted_update=1
THEN 1 ELSE 0 END;
