def check_subject(issue_text: str) -> list[str]:
    lines = issue_text.splitlines()
    if len(lines) == 0 or not lines[0].startswith("Subject:"):
        return ["subject is missing"]
    subject = lines[0][8:].strip()
    if subject == "":
        return ["subject is empty"]
    if len(subject) > 50:
        return ["subject is too long"]
    return []


def check_preview(issue_text: str) -> list[str]:
    lines = issue_text.splitlines()
    if len(lines) < 2 or not lines[1].startswith("Preview:"):
        return ["preview is missing"]
    preview = lines[1][8:].strip()
    if preview == "":
        return ["preview is empty"]
    if len(preview) > 90:
        return ["preview is too long"]
    return []


def check_greeting(issue_text: str) -> list[str]:
    if "{{first_name}}" in issue_text:
        return []
    return ["greeting has no {{first_name}}"]


def check_link(issue_text: str) -> list[str]:
    links = issue_text.count("](http")
    if links == 0:
        return ["link is missing"]
    if links > 1:
        return ["more than one link"]
    return []


def check_footer(issue_text: str) -> list[str]:
    lines = issue_text.strip().splitlines()
    if len(lines) < 2:
        return ["footer is missing"]
    reason = lines[len(lines) - 2]
    unsubscribe = lines[len(lines) - 1]
    if reason.startswith("You're getting this because") and "Unsubscribe: {{unsubscribe_url}}" in unsubscribe:
        return []
    return ["footer is missing"]


def check_issue(issue_text: str) -> list[str]:
    return (
        check_subject(issue_text)
        + check_preview(issue_text)
        + check_greeting(issue_text)
        + check_link(issue_text)
        + check_footer(issue_text)
    )
