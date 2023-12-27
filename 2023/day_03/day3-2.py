from collections import defaultdict
from functools import reduce
from math import prod
import re


def get_digits() -> dict[tuple[int, range], int]:
    """Return a dictionary of digits.

    Digits coordinates as keys (e.g. '(2, 123)' for row 2, column 123).
    Actual digits as values (e.g. '543').

    :return dict[tuple[int, range], int]: dictionary of digits positions and values
    """
    digits = {}
    for n, string in enumerate(strings):
        for digit in re.finditer(r"(\d+)", string):
            start, end = digit.start(), digit.end()
            digits[(n, range(start, end))] = int(digit.group(1))
    return digits


def get_stars() -> list[tuple[int, int]]:
    """Return a list of stars ('*') positions.

    :return list[tuple[int, int]]: list of stars coordinates ([row, column], e.g. ['12', '165'])
    """
    stars = []
    for n, string in enumerate(strings):
        for star in re.finditer(r"(\*)", string):
            stars.append((n, star.start()))
    return stars


def get_gears() -> dict:
    """Return a dictionary of gears.

    Gears coordinates as keys, and adjacent digits as values (e.g. (1, 119): [514, 844])).

    :return dict: dictionary of gears
    """
    gears = defaultdict(list)
    patterns = [
        r"(\d)\.{2}",  # 4..
        r"\.(\d)\.",   # .5.
        r"\.{2}(\d)",  # ..6
        r"(\d{2})\.",  # 45.
        r"\.(\d{2})",  # .56
        r"(\d)\.(\d)", # 4.6
        r"(\d{3})",    # 456
        r"(\d)\*\.",   # 4*.
        r"\.\*(\d)",   # .*6
        r"(\d)\*(\d)", # 4*6
    ]

    # Iterate through stars (i.e. '*')
    for n, idx in stars:
        for row in range(n - 1, n + 2):
            # 3-char string (e.g. '.51')
            chars = strings[row][idx - 1 : idx + 2]

            # Check all patterns
            for pattern in patterns:
                digit_match = re.search(pattern, chars)

                # Add adjacent digit to gear if regex match
                if digit_match:
                    for j in range(len(digit_match.groups())):
                        col = idx + digit_match.span(j + 1)[0] - 1
                        filtered = list(
                            filter(
                                lambda item: row == item[0][0] and col in item[0][1],
                                digits.items(),
                            )
                        )[0]
                        digit = filtered[1]
                        gears[(n, idx)].append(digit)

    # Filter out non-gears (i.e. len <= 1)
    return dict(filter(lambda item: len(item[1]) > 1, gears.items()))


def get_gear_ratios_sum() -> int:
    """Return the sum of all the gear ratios.

    :return int: sum of gear ratios
    """
    return int(
        reduce(
            lambda x, y: x + y,
            map(
                lambda x: prod(x[1]),
                gears.items(),
            ),
        )
    )


if __name__ == "__main__":
    with open("2023/day_03/input.txt", "r") as file:
        strings = file.read().split("\n")
        digits = get_digits()
        stars = get_stars()
        gears = get_gears()
        print(f"Found {len(stars)} stars ⭐️")
        print(f"Found {len(gears)} gears ⚙️")
        print(f"Sum of gear ratios: {get_gear_ratios_sum()}")
