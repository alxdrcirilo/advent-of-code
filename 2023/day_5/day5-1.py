def get_seeds() -> list[int]:
    """Return a list of seeds.

    :return list[int]: list of seeds
    """
    seeds = strings[0][0].split(": ")[1].split(" ")
    seeds = list(map(int, seeds))
    return seeds


def get_value(ranges: list, value: int) -> int:
    """Return the mapped value.

    :param list ranges: value ranges
    :param int value: source value
    :return int: mapped value
    """
    get_value, source, _ = list(map(int, ranges.split(" ")))
    diff = get_value - source
    return diff + value


def get_locations() -> dict[int, int]:
    """Return a dictionary of locations.

    Keys as seeds and locations as values.
    For example:
    ```py
    locations = {
        22: 98,
        12: 37,
        73: 44,
    }
    ```

    :return dict[int, int]: seed locations
    """
    locations = {}
    for seed in seeds:
        # Initial value is seed
        val = seed

        for mapping in strings[1:]:
            # [[50, 98, 2], [52, 50, 48]]
            ranges = [list(map(int, ranges.split(" "))) for ranges in mapping[1:]]

            # [False, True]
            is_in_range = [
                val in range(source, source + span) for _, source, span in ranges
            ]

            # Get the value based on index
            if any(is_in_range):
                idx = is_in_range.index(True)
                val = get_value(mapping[1:][idx], val)

        locations[seed] = val
    return locations


if __name__ == "__main__":
    with open("2023/day_5/input.txt", "r") as file:
        strings = file.read().split("\n\n")
        strings = [string.splitlines() for string in strings]

    seeds = get_seeds()
    locations = get_locations()
    print(f"Lowest location: {min(locations.values())}")
