import maillab

path = "data/subscribers.csv"

total = maillab.count_total(path)
assert total == 24, "expected 24 subscribers in total"

groups = maillab.count_groups(path)
assert groups.get("tea-curious", 0) == 8, "expected 8 in tea-curious"
assert groups.get("gift-buyers", 0) == 8, "expected 8 in gift-buyers"
assert groups.get("daily-drinkers", 0) == 8, "expected 8 in daily-drinkers"

print("All checks passed.")
