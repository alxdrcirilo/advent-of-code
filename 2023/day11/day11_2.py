import itertools
import numpy as np


def get_matrix() -> np.ndarray:
    """Return the matrix.

    For example:
    ```py
    data = [['.' '.' '.' '#' '.' '.' '.' '.' '.' '.']
            ['.' '.' '.' '.' '.' '.' '.' '#' '.' '.']
            ['#' '.' '.' '.' '.' '.' '.' '.' '.' '.']
            ['.' '.' '.' '.' '.' '.' '.' '.' '.' '.']
            ['.' '.' '.' '.' '.' '.' '#' '.' '.' '.']
            ['.' '#' '.' '.' '.' '.' '.' '.' '.' '.']
            ['.' '.' '.' '.' '.' '.' '.' '.' '.' '#']
            ['.' '.' '.' '.' '.' '.' '.' '.' '.' '.']
            ['.' '.' '.' '.' '.' '.' '.' '#' '.' '.']
            ['#' '.' '.' '.' '#' '.' '.' '.' '.' '.']]
    ```

    :return np.array: matrix
    """
    with open("2023/day_11/input.txt", "r") as file:
        data = file.read().splitlines()
        data = [list(line.strip()) for line in data]
    return np.array(data)


def get_pairs() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """Return all the combinations of galaxies with their coordinates.

    :return list[tuple[tuple[int, int], tuple[int, int]]]: combinations [((row, col), (row, col)), ...]
    """
    return list(itertools.combinations(galaxies.values(), 2))


def get_empty_rows_cols(data: np.ndarray) -> tuple:
    """Return empty rows and columns.

    :return list: list of empty rows and columns
    """
    # Get empty rows and columns
    empty_rows = np.all(data == ".", axis=1)
    empty_cols = np.all(data == ".", axis=0)

    # Get the indices of empty rows and columns
    empty_row_indices = np.where(empty_rows)[0]
    empty_col_indices = np.where(empty_cols)[0]
    return (empty_row_indices, empty_col_indices)


def get_galaxies() -> dict[int, tuple[int, int]]:
    """Return the galaxies coordinates.

    :return dict[int, tuple[int, int]]: galaxies
    """
    galaxies = {}
    for n, (row, col) in enumerate(np.column_stack(np.where(data == "#"))):
        data[row][col] = n + 1
        galaxies[n + 1] = (row, col)
    return galaxies


def get_manhattan_distance(pair: tuple[tuple[int, int], tuple[int, int]]) -> int:
    """Return the Manhattan distance between two coordinates.

    Scale included to deal with 1E6 increment for empty rows/columns.

    :param tuple[tuple[int, int], tuple[int, int]] pair: pair of coordinates
    :return int: Manhattan distance
    """
    source, target = pair
    scale = (int(1e6) - 1) * len(
        set(range(min(source[0], target[0]), max(source[0], target[0])))
        & set(empty_row_indices)
    )
    scale += (int(1e6) - 1) * len(
        set(range(min(source[1], target[1]), max(source[1], target[1])))
        & set(empty_col_indices)
    )
    return scale + abs(source[0] - target[0]) + abs(source[1] - target[1])


if __name__ == "__main__":
    data = get_matrix()
    empty_row_indices, empty_col_indices = get_empty_rows_cols(data)
    galaxies = get_galaxies()
    pairs = get_pairs()

    result = sum(map(get_manhattan_distance, pairs))
    print(f"Sum of all {len(pairs)} shortest paths: {result}")
