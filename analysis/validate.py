"""Validate CSV contracts and execute the supplied SQL against the same rows."""
import argparse
import csv
import json
import sqlite3
from collections import Counter
from pathlib import Path
from generate_fixture import FIELDS, FLAGS, PLAN, generate

ROOT = Path(__file__).resolve().parents[1]

def validate(path):
    with path.open(newline='', encoding='utf-8') as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != FIELDS:
            raise ValueError('Unexpected CSV schema')
        rows = list(reader)
    if len(rows) != 800 or len({row['case_id'] for row in rows}) != len(rows):
        raise ValueError('Expected 800 unique case IDs')
    counts, flagged = Counter(), Counter()
    for row in rows:
        for field in [*FLAGS, 'communication_exception']:
            if row[field] not in ('0', '1'):
                raise ValueError(f'Non-binary flag: {field}')
        if str(int(any(row[field] == '1' for field in FLAGS))) != row['communication_exception']:
            raise ValueError('Union flag mismatch')
        contact = int(row['repeat_contacts_7d'])
        if contact < 0 or str(contact) != row['repeat_contacts_7d']:
            raise ValueError('Invalid contact count')
        counts[row['review_type']] += 1
        flagged[row['review_type']] += int(row['communication_exception'])
    if counts != Counter({kind: count for kind, count, _ in PLAN}):
        raise ValueError('Category counts differ from the fixture contract')
    if flagged != Counter({kind: count for kind, _, count in PLAN}):
        raise ValueError('Injected exception counts differ from the fixture contract')
    connection = sqlite3.connect(':memory:')
    schema = ','.join(f'{field} {"TEXT" if field in FIELDS[:2] else "INTEGER"}' for field in FIELDS)
    connection.execute(f'CREATE TABLE synthetic_review_cases ({schema})')
    connection.executemany('INSERT INTO synthetic_review_cases VALUES (' + ','.join('?' for _ in FIELDS) + ')',
                           [[row[field] for field in FIELDS] for row in rows])
    sql = (ROOT / 'analysis/qa_queries.sql').read_text(encoding='utf-8')
    queries = ['\n'.join(line for line in part.splitlines() if not line.strip().startswith('--')).strip()
               for part in sql.split(';')]
    results = [connection.execute(query).fetchall() for query in queries if query]
    if results[1] != []:
        raise ValueError('SQL reconciliation returned exceptions')
    connection.close()
    return {'file': path.name, 'rows': len(rows), 'summary': results[0], 'union_mismatches': 0}

def verify_generator():
    if generate(42) != generate(42) or generate(42) == generate(43):
        raise ValueError('Generator determinism check failed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', nargs='?', type=Path, default=ROOT / 'data/synthetic_review_cases.csv')
    args = parser.parse_args()
    verify_generator()
    print(json.dumps(validate(args.csv), indent=2))
