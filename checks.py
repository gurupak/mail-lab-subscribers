from datetime import date

import maillab

path = "data/subscribers.csv"

total = maillab.count_total(path)
assert total == 24, "expected 24 subscribers in total"

groups = maillab.count_groups(path)
assert groups.get("tea-curious", 0) == 8, "expected 8 in tea-curious"
assert groups.get("gift-buyers", 0) == 8, "expected 8 in gift-buyers"
assert groups.get("daily-drinkers", 0) == 8, "expected 8 in daily-drinkers"

run_date = date.fromisoformat("2026-11-20")
# 7 includes 2026-10-21 (exactly 30 days back) and leaves out 2026-10-20.
assert maillab.count_since(path, run_date, 30) == 7, "expected 7 joined in the last 30 days"

assert maillab.next_send(date.fromisoformat("2026-11-20")) == date.fromisoformat("2026-12-07"), "expected next send 2026-12-07"
assert maillab.next_send(date.fromisoformat("2026-12-07")) == date.fromisoformat("2027-01-04"), "expected next send 2027-01-04"

print("All checks passed.")
