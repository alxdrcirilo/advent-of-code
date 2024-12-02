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


def get_impossible_games() -> set[int]:
    """Get IDs of impossible games.

    :return set[int]: set of IDs of impossible games
    """
    bag = {"red": 12, "green": 13, "blue": 14}
    impossible_games = set()
    for k, v in games.items():
        rollout = get_rollout(v)
        for subset in rollout:
            for color, cubes in subset.items():
                if cubes > bag[color]:
                    game_id = int(k.removeprefix("Game "))
                    impossible_games.add(game_id)
                else:
                    pass
    return impossible_games


if __name__ == "__main__":
    with open("2023/day02/input.txt", "r") as file:
        strings = file.read().split("\n")

        # Parse to human-readable format
        strings = list(map(lambda x: x.split(":"), strings))
        games = {k: v.split(";") for k, v in strings}

        # Substract impossible game set to full game set
        full_games = set(range(1, 101))
        impossible_games = get_impossible_games()
        possible_games = full_games - impossible_games

        # Sum of possible games IDs
        print(f"Sum of the IDs of games: {sum(possible_games)}")
