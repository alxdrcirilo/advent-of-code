import re


def is_symbol(char: str) -> bool:
    """Check if a character is a symbol.

    :param str char: e.g. 'A'
    :return bool: True if char is a symbol, False otherwise
    """
    symbols = set("&+/#@$%=*-")
    return char in symbols


def get_sum() -> int:
    """Return the sum of the part numbers.

    :return int: sum of the part numbers
    """
    sum = 0
    for n, string in enumerate(strings):
        for digit_match in re.finditer(r"(\d+)", string):
            start, end = (
                max(0, digit_match.start() - 1),
                min(140, digit_match.end() + 1),
            )
            prev_line, next_line = max(0, n - 1), min(len(strings), n + 2)
            for string_subset in strings[prev_line:next_line]:
                if any(list(map(is_symbol, string_subset[start:end]))):
                    sum += int(digit_match.group(1))
                    break
    return sum


if __name__ == "__main__":
    with open("2023/day_3/input.txt", "r") as file:
        strings = file.read().split("\n")
        print(f"Sum of part numbers: {get_sum()}")
