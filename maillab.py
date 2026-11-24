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
    return 0


def count_groups(path: str) -> dict[str, int]:
    return {}
