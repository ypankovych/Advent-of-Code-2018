def prepare(data):
    coordinates = set()
    max_row = 0
    max_column = 0

    for line in data:
        r, c = map(int, line.split(", "))
        coordinates.add((r, c))
        max_row = max(max_row, r)
        max_column = max(max_column, c)
    return coordinates, max_column, max_row


def main(data, manhattan_limit=10000):
    coordinates, max_row, max_column = prepare(data)
    region_size = 0

    for i in range(max_row + 1):
        for j in range(max_column + 1):
            region_size += int(sum(abs(r - i) + abs(c - j) for r, c in coordinates) < manhattan_limit)

    return region_size


if __name__ == '__main__':
    print(main([line.strip() for line in open('data.txt').readlines()]))
