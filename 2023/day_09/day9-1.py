def get_diff_sum(values: list[int]) -> int:
    """Return the sum of the extrapolated values.

    :return int: sum of extrapolated values
    """
    diff = [b - a for a, b in zip(values, values[1:])]
    while any(diff):
        return values[-1] + get_diff_sum(diff)
    return values[-1]


if __name__ == "__main__":
    with open("2023/day_09/input.txt", "r") as file:
        data = file.read().splitlines()

    data = [list(map(int, line.split())) for line in data]
    print(f"Sum of the extrapolated values: {sum(map(get_diff_sum, data))}")
