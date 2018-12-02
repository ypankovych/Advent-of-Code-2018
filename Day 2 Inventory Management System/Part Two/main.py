def get_data():
    with open('data.txt') as f:
        return list(map(str.strip, f.readlines()))


def calculate(elem, item):
    diff_count = 0
    temp_index = 0
    index = 0
    for first, second in zip(elem, item):
        if first != second:
            diff_count += 1
            index = temp_index
        temp_index += 1
    if diff_count == 1:
        print(item[:index] + item[index + 1:])


def main(data):
    for index, elem in enumerate(data):
        for item in data[index:]:
            calculate(elem, item)


if __name__ == '__main__':
    main(get_data())
