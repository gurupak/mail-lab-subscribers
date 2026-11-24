import sys
from datetime import date, timedelta


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
    start = run_date - timedelta(days=days)
    count = 0
    for row in read_rows(path):
        joined = date.fromisoformat(row[4])
        if start <= joined and joined <= run_date:
            count = count + 1
    return count


def next_send(run_date: date) -> date:
    if run_date.month == 12:
        day = date(run_date.year + 1, 1, 1)
    else:
        day = date(run_date.year, run_date.month + 1, 1)
    while day.weekday() != 0:  # 0 is Monday
        day = day + timedelta(days=1)
    return day


if len(sys.argv) > 1:
    command = sys.argv[1]
    since_days = 0
    run_date = date.today()  # the only place that reads today's date
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--since-days":
            since_days = int(sys.argv[i + 1])
        elif sys.argv[i] == "--run-date":
            run_date = date.fromisoformat(sys.argv[i + 1])
        i = i + 2

    if command == "subscribers":
        path = "data/subscribers.csv"
        print("Total:", count_total(path))
        groups = count_groups(path)
        for group in sorted(groups):
            print(group + ":", groups[group])
        if since_days > 0:
            print("Run date:", run_date)
            print("Joined in the last", since_days, "days:", count_since(path, run_date, since_days))
    elif command == "next-send":
        print("Run date:", run_date)
        print("Next send:", next_send(run_date))
