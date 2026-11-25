from datetime import date

import maillab

path = "data/subscribers.csv"


def test_total_counts_every_subscriber():
    assert maillab.count_total(path) == 24


def test_each_group_has_eight_subscribers():
    groups = maillab.count_groups(path)
    assert groups.get("tea-curious", 0) == 8
    assert groups.get("gift-buyers", 0) == 8
    assert groups.get("daily-drinkers", 0) == 8


def test_last_30_days_includes_the_30th_day_back():
    # 7 includes 2026-10-21 (exactly 30 days back) and leaves out 2026-10-20.
    run_date = date.fromisoformat("2026-11-20")
    assert maillab.count_since(path, run_date, 30) == 7


def test_next_send_is_first_monday_of_next_month():
    run_date = date.fromisoformat("2026-11-20")
    assert maillab.next_send(run_date) == date.fromisoformat("2026-12-07")


def test_next_send_in_december_moves_into_next_year():
    run_date = date.fromisoformat("2026-12-07")
    assert maillab.next_send(run_date) == date.fromisoformat("2027-01-04")
