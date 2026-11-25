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


def test_short_subject_has_no_problems():
    text = "Subject: The Steep Club opens Monday\nPreview: Your monthly tea box.\n"
    assert maillab.check_subject(text) == []


def test_subject_of_50_characters_has_no_problems():
    text = "Subject: Your Steep Club box ships on Monday with new teas.\nPreview: Your monthly tea box.\n"
    assert maillab.check_subject(text) == []


def test_subject_of_51_characters_is_too_long():
    text = "Subject: Your Steep Club box ships on Monday with fresh teas\nPreview: Your monthly tea box.\n"
    assert maillab.check_subject(text) == ["subject is too long"]


def test_empty_subject_is_empty():
    text = "Subject:\nPreview: Your monthly tea box.\n"
    assert maillab.check_subject(text) == ["subject is empty"]


def test_subject_of_only_spaces_is_empty():
    text = "Subject:     \nPreview: Your monthly tea box.\n"
    assert maillab.check_subject(text) == ["subject is empty"]


def test_no_subject_line_is_missing():
    text = "Preview: Your monthly tea box.\n\nHi {{first_name}},\n"
    assert maillab.check_subject(text) == ["subject is missing"]
