def read_issue(path: str) -> str:
    with open(path) as file:
        return file.read()
