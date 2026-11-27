import sys
from datetime import date

from maillab.checks import check_issue
from maillab.dates import next_send
from maillab.issue import read_issue
from maillab.subscribers import count_groups, count_since, count_total


def main() -> None:
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
        elif command == "check":
            text = read_issue(sys.argv[2])
            problems = check_issue(text)
            if len(problems) == 0:
                print("OK")
            else:
                for problem in problems:
                    print(problem)
                sys.exit(1)


if __name__ == "__main__":
    main()
