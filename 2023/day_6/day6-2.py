def count_records() -> int:
    """Return the number of ways to beat the record.

    To quickly compute this, simply get the first and last breakpoints.
    The difference between these represents the number of ways to be the record.

    :return int: count of ways to beat the record
    """
    data = []
    for line in lines:
        data.append(int("".join(line[1].split())))

    time, dist = data
    breakpoints = []
    ranges = [range(time + 1), range(time + 1, 0, -1)]
    for r in ranges:
        for speed in r:
            remaining_time = time - speed
            travelled_dist = speed * remaining_time
            if travelled_dist < dist:
                continue
            else:
                breakpoints.append(speed)
                break
    return breakpoints[1] - breakpoints[0] + 1


if __name__ == "__main__":
    with open("2023/day_6/input.txt", "r") as file:
        lines = file.read().splitlines()
        lines = [x.split(":") for x in lines]

    result = count_records()
    print(f"Number of ways you can beat the record: {result}")
