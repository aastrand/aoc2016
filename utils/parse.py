import re


def ints(str):
    return [int(s) for s in re.findall(r"-?\d+", str)]
