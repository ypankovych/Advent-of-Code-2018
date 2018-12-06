from collections import defaultdict


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


def main(data):
    coordinates, max_row, max_column = prepare(data)
    infinite = set()
    sizes = defaultdict(int)
    points = {index: point for index, point in enumerate(coordinates, start=1)}

    for i in range(max_row + 1):
        for j in range(max_column + 1):
            min_dists = sorted([(abs(r - i) + abs(c - j), coord) for coord, (r, c) in points.items()])
            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                sizes[coord_id] += 1
                if i == 0 or i == max_row or j == 0 or j == max_column:
                    infinite.add(coord_id)

    return max(size for coord_id, size in sizes.items() if coord_id not in infinite)


if __name__ == '__main__':
    print(main([line.strip() for line in open('data.txt').readlines()]))
