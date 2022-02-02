import re
import sys

changes_types = [
    "fix",
    "feat",
    "build",
    "chore",
    "ci",
    "docs",
    "style",
    "refactor",
    "perf",
    "test",
    "misc",
]

regexp = re.compile(r"^(%s)\(\w+\)?!?:\s(.*)$" % "|".join(changes_types))
with open(sys.argv[1], "r") as f:
    data = f.read()
    matched = regexp.match(data)
    if matched is None:
        print("Please use the correct commit message format.")
        exit(-1)
    if len(matched.group(0)) < 15:
        print(
            "Please describe the change in detail. \n"
            + "Example: 'feat(api): send an email to the customer'"
        )
        exit(-1)
exit(0)
