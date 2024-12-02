from functools import reduce


def count_records() -> int:
    """Return the number of ways to beat the record.

    :return int: count of ways to beat the record
    """
    data = []
    for line in lines:
        data.append(list(map(int, line[1].split())))
    data = list(zip(data[0], data[1]))

    logs = []
    for time, dist in data:
        counter = 0
        for speed in range(time + 1):
            remaining_time = time - speed
            travelled_dist = speed * remaining_time
            if travelled_dist > dist:
                counter += 1
        logs.append(counter)

    result = reduce(lambda x, y: x * y, logs)
    return result


if __name__ == "__main__":
    with open("2023/day06/input.txt", "r") as file:
        lines = file.read().splitlines()
        lines = [x.split(":") for x in lines]

    result = count_records()
    print(f"Number of ways you can beat the record: {result}")
