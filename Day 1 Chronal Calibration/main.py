def get_data():
    with open('data.txt') as f:
        return map(int, f.readlines())


def main(data):
    return sum(data)


if __name__ == '__main__':
    print(main(get_data()))
