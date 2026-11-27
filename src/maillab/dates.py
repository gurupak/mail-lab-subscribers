from datetime import date, timedelta


def next_send(run_date: date) -> date:
    if run_date.month == 12:
        day = date(run_date.year + 1, 1, 1)
    else:
        day = date(run_date.year, run_date.month + 1, 1)
    while day.weekday() != 0:  # 0 is Monday
        day = day + timedelta(days=1)
    return day
