from collections import Counter


def get_data():
    with open('data.txt') as f:
        return map(str.strip, f.readlines())


def calculate(elem, c):
    for count in Counter(elem).values():
        if count == c:
            return True
    return False


def main(data):
    twice = 0
    three = 0
    for i in data:
        twice += calculate(i, 2)
        three += calculate(i, 3)
    return twice * three


if __name__ == '__main__':
    print(main(get_data()))
