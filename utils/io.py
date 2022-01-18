def get_lines(filename):
    return [l.strip() for l in open(filename, "r")]


def get_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()
