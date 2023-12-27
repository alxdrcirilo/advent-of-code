import re


def get_points(scratchcard: str) -> int:
    """Return the total number of points of a scratchcard.

    Computes the total number of points worth based on the given pattern.
    
    :param str scratchcard: scratchcard (e.g. `Card   1: 69 12 75 ... | 83 63 56 ...`)
    :return int: total number of points
    """
    result = re.match(pattern, scratchcard)
    _, own, win = [[*map(int, x.split())] for x in result.groups()]
    intersection = len(set(own) & set(win)) - 1
    return int(2**intersection)


if __name__ == "__main__":
    with open("2023/day_04/input.txt", "r") as file:
        data = file.read().splitlines()

    pattern = r"Card\s+(\d+):(?:\s+)((?:\d+\s*)+)\s\|(?:\s+)((?:\d+\s*)+)"
    points = sum(map(lambda x: get_points(x), data))
    print(f"Total number of points: {points}")
