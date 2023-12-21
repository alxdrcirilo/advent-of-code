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


def expand_matrix(data: np.ndarray) -> np.ndarray:
    """Expand the matrix if row/col is empty.

    :param np.ndarray data: original matrix
    :return np.ndarray: expanded matrix
    """
    # Get empty rows and columns
    empty_rows = np.all(data == ".", axis=1)
    empty_cols = np.all(data == ".", axis=0)

    # Get the indices of empty rows and columns
    empty_row_indices = np.where(empty_rows)[0]
    empty_col_indices = np.where(empty_cols)[0]

    data = np.insert(data, empty_row_indices, ".", axis=0)
    data = np.insert(data, empty_col_indices, ".", axis=1)
    return data


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

    :param tuple[tuple[int, int], tuple[int, int]] pair: pair of coordinates
    :return int: Manhattan distance
    """
    source, target = pair
    return abs(source[0] - target[0]) + abs(source[1] - target[1])


if __name__ == "__main__":
    data = get_matrix()
    data = expand_matrix(data)
    galaxies = get_galaxies()
    pairs = get_pairs()

    result = sum(map(get_manhattan_distance, pairs))
    print(f"Sum of all {len(pairs)} shortest paths: {result}")
