def get_grid() -> dict[tuple[int, int], str]:
    """Return the grid.

    Keys as (row, column) coordinates, and values as character (e.g. 'J').

    :return dict[tuple[int, int], int]: grid
    """
    grid = {}
    for row, line in enumerate(data):
        for col, val in enumerate(line):
            grid[row, col] = val
    return grid


def get_source() -> tuple[int, int]:
    """Return the source node (e.g. (1, 1)).

    :return tuple[int, int]: source node
    """
    return [(row, col) for (row, col), val in grid.items() if val == "S"][0]


def get_farthest_steps() -> int:
    """Return the number of steps to the farthest point in the loop from the source.

        - `|` is a vertical pipe connecting north and south.
        - `-` is a horizontal pipe connecting east and west.
        - `L` is a 90-degree bend connecting north and east.
        - `J` is a 90-degree bend connecting north and west.
        - `7` is a 90-degree bend connecting south and west.
        - `F` is a 90-degree bend connecting south and east.
        - `.` is ground; there is no pipe in this tile.
        - `S` is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    :return int: number of steps to the farthest point
    """
    visited = {source}
    queue = [source]
    nrow = len(set([row for row, _ in grid.keys()]))
    ncol = len(set([col for _, col in grid.keys()]))

    while queue:
        row, col = queue.pop(0)
        char = grid[(row, col)]

        if (
            row > 0
            and char in "S|JL"
            and grid[(row - 1, col)] in "|7F"
            and (row - 1, col) not in visited
        ):
            visited.add((row - 1, col))
            queue.append((row - 1, col))

        if (
            row < nrow - 1
            and char in "S|7F"
            and grid[(row + 1, col)] in "|JL"
            and (row + 1, col) not in visited
        ):
            visited.add((row + 1, col))
            queue.append((row + 1, col))

        if (
            col > 0
            and char in "S-J7"
            and grid[(row, col - 1)] in "-LF"
            and (row, col - 1) not in visited
        ):
            visited.add((row, col - 1))
            queue.append((row, col - 1))

        if (
            col < ncol - 1
            and char in "S-LF"
            and grid[(row, col + 1)] in "-J7"
            and (row, col + 1) not in visited
        ):
            visited.add((row, col + 1))
            queue.append((row, col + 1))
    return len(visited) // 2


if __name__ == "__main__":
    # Source: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day10p1.py
    with open("2023/day10/input.txt", "r") as file:
        data = file.read().splitlines()

    grid = get_grid()
    source = get_source()
    result = get_farthest_steps()
    print(f"Number of steps to the farthest point: {result}")
