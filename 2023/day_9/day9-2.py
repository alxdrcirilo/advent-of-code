def get_diff_sum(values: list[int]) -> int:
    """Return the sum of the extrapolated values (backwards).

    :return int: sum of extrapolated values
    """
    diff = [b - a for a, b in zip(values, values[1:])]
    while any(diff):
        return values[0] - get_diff_sum(diff)
    return values[0]


if __name__ == "__main__":
    with open("2023/day_9/input.txt", "r") as file:
        data = file.read().splitlines()

    data = [list(map(int, line.split())) for line in data]
    print(f"Sum of the extrapolated values (backwards): {sum(map(get_diff_sum, data))}")
