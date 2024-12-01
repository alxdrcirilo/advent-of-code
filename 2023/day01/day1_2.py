import re


def extract_digits_extended(string: str) -> int:
    """Extract two-digit number from a string (first and last) in extended format, including overlaps.

    For example, '2abc3oneeight' should return '28'.

    :param str string: string (e.g. '1abc2')
    :return int: two-digit number (e.g. 12)
    """

    mapping = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "d": "\d",
    }
    
    # Extract digits using regex (only keep start() and group() from Match objects)
    matches = list(
        map(
            lambda word: [(x.start(), x.group(0)) for x in re.finditer(word, string)],
            mapping.values(),
        )
    )

    # Filter out emtpy matches, flatten, and sort
    matches = list(filter(lambda x: x, matches))
    matches = [submatch for match in matches for submatch in match]
    matches = sorted(matches, key=lambda x: x[0])

    # Duplicate when only one match is found
    if len(matches) == 1:
        matches = matches * 2

    # Keep first and last results only
    head, *_, tail = matches
    digits = [head[1], tail[1]]

    # Try to cast to int
    for n, digit in enumerate(digits):
        try:
            int(digit)
        except ValueError:
            for k, v in mapping.items():
                if digit == v:
                    digits[n] = k

    return int("".join(digits))


if __name__ == "__main__":
    with open("2023/day_01/input.txt", "r") as file:
        strings = file.read().split("\n")
        sum = sum(list(map(extract_digits_extended, strings)))
        print(f"Sum of calibration values (extended): {sum}")
