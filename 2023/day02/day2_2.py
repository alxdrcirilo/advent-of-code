from functools import reduce
import re


def get_rollout(game: list) -> list[dict]:
    """Extract game information (rollout).

    :param list game: list of sets (e.g. ['1 green, 1 blue, 1 red', ' 1 green, 8 red, 7 blue'])
    :return list[dict]: dictionary of sets (e.g. [{'red': 1, 'green': 1, 'blue': 1}, {'red': 8, 'green': 1, 'blue': 7}])
    """
    sets = []
    colors = ("red", "green", "blue")
    for rollout in game:
        subset = {}
        for color in colors:
            # Find matches
            match = re.match(rf".*\s(\d+)\s{color}.*", rollout)
            # Extract first capture group
            if match:
                subset[color] = int(match.group(1))
            else:
                subset[color] = 0
        sets.append(subset)
    return sets


def get_power_sets() -> list[int]:
    """Return all power sets.

    :return list[int]: list of power sets.
    """
    colors = ("red", "green", "blue")
    power_sets = []

    # Extract minimum number of cubes per game
    for game in games.values():
        rollout = get_rollout(game)
        minimum_cubes = {}
        for color in colors:
            minimum_cubes[color] = max([subset[color] for subset in rollout])
        power_sets.append(reduce(lambda x, y: x * y, minimum_cubes.values()))
    return power_sets


if __name__ == "__main__":
    with open("2023/day_02/input.txt", "r") as file:
        strings = file.read().split("\n")

        # Parse to human-readable format
        strings = list(map(lambda x: x.split(":"), strings))
        games = {k: v.split(";") for k, v in strings}

        # Sum power of all sets
        power_sets = get_power_sets()
        print(f"Sum of power sets: {sum(power_sets)}")
