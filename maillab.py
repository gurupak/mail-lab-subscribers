import sys
from datetime import date


def read_rows(path: str) -> list[list[str]]:
    with open(path) as file:
        text = file.read()
    lines = text.splitlines()
    header = lines[0]
    rows = []
    for line in lines:
        if line != header:
            rows.append(line.split(","))
    return rows


def count_total(path: str) -> int:
    return len(read_rows(path))


def count_groups(path: str) -> dict[str, int]:
    groups: dict[str, int] = {}
    for row in read_rows(path):
        group = row[3]
        groups[group] = groups.get(group, 0) + 1
    return groups


def count_since(path: str, run_date: date, days: int) -> int:
    return 0


def next_send(run_date: date) -> date:
    return run_date


if len(sys.argv) > 1 and sys.argv[1] == "subscribers":
    path = "data/subscribers.csv"
    print("Total:", count_total(path))
    groups = count_groups(path)
    for group in sorted(groups):
        print(group + ":", groups[group])
