import re


def get_points(pattern: str) -> int:
    """Return the total number of points.

    Computes the total number of points worth based on the given pattern.

    :param str pattern: regex pattern
    :return int: total number of points
    """
    points = 0
    for string in strings:
        res = re.match(pattern, string)
        if res:
            # Split into card, owned, and won numbers
            numbers_str = list(map(lambda x: re.split(r"\s+", x), res.groups()))
            # Cast to int
            numbers_int = list(map(lambda x: [int(y) for y in x], numbers_str))
            # Extract attributes
            own_numbers = set(numbers_int[1])
            win_numbers = set(numbers_int[2])
            # Compute intersection
            intersection = len(own_numbers & win_numbers) - 1
            points += int(2**intersection)
    
    return points


if __name__ == "__main__":
    with open("2023/day_4/input.txt", "r") as file:
        strings = file.read().split("\n")
        pattern = r"Card\s+(\d+):(?:\s+)((?:\d+\s*)+)\s\|(?:\s+)((?:\d+\s*)+)"
        points = get_points(pattern)
        print(f"Total number of points: {points}")
