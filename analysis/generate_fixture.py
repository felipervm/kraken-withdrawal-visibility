"""Generate an additional synthetic fixture; does not reconstruct the original CSV."""
import argparse
import csv
import random
from pathlib import Path

FLAGS = ['status_stale', 'missing_support_reference', 'cross_channel_mismatch', 'missed_permitted_update']
FIELDS = ['case_id', 'review_type', *FLAGS, 'repeat_contacts_7d', 'communication_exception']
PLAN = [('scheduled_hold', 412, 40), ('manual_review', 302, 150), ('transient_display', 86, 42)]

def generate(seed=42):
    rng = random.Random(seed)
    rows = []
    for category, count, flagged in PLAN:
        for index in range(count):
            # Fixed counts are arbitrary demonstration inputs, never Kraken estimates.
            bits = [0] * len(FLAGS)
            if index < flagged:
                for position in rng.sample(range(len(FLAGS)), rng.randint(1, len(FLAGS))):
                    bits[position] = 1
            exception = int(any(bits))
            rows.append(dict(review_type=category, **dict(zip(FLAGS, bits)),
                             repeat_contacts_7d=rng.randrange(4 if exception else 2),
                             communication_exception=exception))
    rng.shuffle(rows)
    return [dict(case_id=f'G-{index:04d}', **row) for index, row in enumerate(rows, 1)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'data/generated_review_cases.csv')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', newline='', encoding='utf-8') as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(generate(args.seed))
    print(f'Wrote 800 entirely synthetic cases to {args.output}')
