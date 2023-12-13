import re


def get_mapping() -> dict[str, tuple[str, str]]:
    """Return a mapping of nodes.

    For example:
    ```py
    mapping = {
        'FSH': ('CGN', 'NDK'),
        ...
    }
    ```

    :return dict[int, tuple[int, int]]: mapping of nodes
    """
    mapping = {}
    for line in nodes:
        pattern = r"(\w{3}) = \((\w{3}), (\w{3})\)"
        match = re.match(pattern, line)
        if match:
            a, b, c = [match.group(i) for i in range(1, 4)]
            mapping[a] = (b, c)
    return mapping


def get_steps(start: str, target: str, mapping: dict) -> int:
    """Return the number of steps required to go from start to target.

    :param str start: start node (e.g. 'AAA')
    :param str target: target node (e.g. 'ZZZ')
    :param dict mapping: mapping of nodes
    :return int: number of steps required to go from start to target
    """
    counter = 0
    node = start
    while node != target:
        direction = directions[counter % len(directions)]
        if direction == "L":
            node = mapping[node][0]
        elif direction == "R":
            node = mapping[node][1]
        counter += 1
    return counter


if __name__ == "__main__":
    with open("2023/day_8/input.txt", "r") as file:
        directions, _, *nodes = file.read().splitlines()

    mapping = get_mapping()
    result = get_steps(start="AAA", target="ZZZ", mapping=mapping)
    print(f"Steps from 'AAA' to 'ZZZ': {result}")
