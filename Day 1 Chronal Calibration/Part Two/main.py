from itertools import cycle


def get_data():
    with open('data.txt') as f:
        return map(int, f.readlines())


def main(data):
    res = set()
    count = 0
    for value in cycle(data):
        count += value
        if count in res:
            return count
        res.add(count)


if __name__ == '__main__':
    print(main(get_data()))
