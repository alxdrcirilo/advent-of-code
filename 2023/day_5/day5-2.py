from collections import defaultdict


def get_seeds() -> list[int]:
    """Return a list of seeds.

    :return list[int]: list of seeds
    """
    seeds = strings[0][0].split(": ")[1].split(" ")
    seeds = list(map(int, seeds))
    return seeds


def get_blocks() -> defaultdict[list[int]]:
    """Return a dictionary of mappings.

    For example:
    ```py
    blocks = {
        'seed-to-soil':
            [
                (50, 98, 2),
                (52, 50, 40),
            ],
        'soil-to-fertilizer':
            [
                (0, 15, 37),
                (37, 52, 2),
                (39, 0, 15),
            ],
        ...
    }
    ```

    :return defaultdict[list[int]]: dictionary of mappings
    """
    blocks = defaultdict(list)
    for title, *data in strings[1:]:
        title = title.removesuffix(" map:")
        for subdata in data:
            dest, src, span = [int(x) for x in subdata.split()]
            blocks[title].append((dest, src, span))
    return blocks


def get_lowest_location(seeds: list[tuple[int, int]]) -> int:
    """Return the lowest location based on seed ranges.

    :param list[tuple[int, int]] seeds: seed ranges
    :return int: lowest location
    """
    for block in blocks.values():
        new = []
        while seeds:
            start, end = seeds.pop()
            for dest, src, span in block:
                overlap_start = max(start, src)
                overlap_end = min(end, src + span)
                if overlap_start < overlap_end:
                    new.append((overlap_start - src + dest, overlap_end - src + dest))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new
    return min(seeds)[0]


if __name__ == "__main__":
    with open("2023/day_5/input.txt", "r") as file:
        strings = file.read().split("\n\n")
        strings = [string.splitlines() for string in strings]

    seeds = get_seeds()
    seeds = [(start, start + span) for start, span in zip(seeds[::2], seeds[1::2])]
    blocks = get_blocks()
    lowest_location = get_lowest_location(seeds)
    print(f"Lowest location (ranges): {lowest_location}")
