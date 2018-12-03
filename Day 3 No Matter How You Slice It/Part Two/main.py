from collections import defaultdict


def get_values(line):
    ids, _, offset, d = line.split()
    left, top = offset[:-1].split(",")
    width, height = d.split("x")
    return ids, int(left), int(top), int(width), int(height)


def get_data():
    with open('data.txt') as fp:
        return fp.readlines()


def main(data):
    vals = [get_values(line) for line in data]
    fabric = defaultdict(int)
    for _, l, t, w, h in vals:
        for i in range(w):
            for j in range(h):
                fabric[(i + l, j + t)] += 1

    for ids, l, t, w, h in vals:
        flag = True
        for i in range(w):
            for j in range(h):
                if fabric[(i + l, j + t)] != 1:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            return ids[1:]


if __name__ == '__main__':
    print(main(get_data()))
