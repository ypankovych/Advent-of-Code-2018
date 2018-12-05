from re import sub
from string import ascii_uppercase, ascii_lowercase


def get_pairs():
    pairs = []
    for i, j in zip(ascii_uppercase, ascii_lowercase):
        pairs.append(f'{i+j}')
        pairs.append(f'{j+i}')
    return pairs


def main(data):
    prev = data
    while True:
        res = sub('|'.join(get_pairs()), '', prev)
        if res == prev:
            return len(res)
        prev = res


if __name__ == '__main__':
    print(main(open('data.txt').read()))
