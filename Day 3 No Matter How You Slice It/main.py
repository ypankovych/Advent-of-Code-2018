from collections import defaultdict


def get_data():
    with open('data.txt') as fp:
        return fp.readlines()


def get_values(line):
    ids, _, offset, d = line.split()
    left, top = offset[:-1].split(",")
    width, height = d.split("x")
    return ids, int(left), int(top), int(width), int(height)


def main(data):
    vals = [get_values(line) for line in data]
    fabric = defaultdict(int)
    for _, l, t, w, h in vals:
        for i in range(w):
            for j in range(h):
                fabric[(i + l, j + t)] += 1

    total = 0
    for v in fabric.values():
        if v > 1:
            total += 1
    return total


if __name__ == '__main__':
    print(main(get_data()))
