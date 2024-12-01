def extract_digits(string: str) -> int:
    """Extract two-digit number from a string (first and last).

    :param str string: string (e.g. '1abc2')
    :return int: two-digit number (e.g. 12)
    """
    digits = [str(x) for x in string if x.isdigit()]

    if len(digits) == 1:
        return int(f"{digits[0] * 2}")
    elif len(digits) == 2:
        return int("".join(digits))
    else:
        head, *_, tail = digits
        return int(f"{head}{tail}")


if __name__ == "__main__":
    with open("2023/day_01/input.txt", "r") as file:
        strings = file.read().split("\n")
        digits = list(map(extract_digits, strings))
        print(f"Sum of calibration values: {sum(digits)}")
