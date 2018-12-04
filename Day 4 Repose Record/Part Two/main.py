import datetime as dt
from collections import Counter, defaultdict

dt_format = '[%Y-%m-%d %H:%M'


def get_data():
    with open('data.txt') as fp:
        return sorted(map(str.strip, fp.readlines()))


def extract_datetime(item):
    return dt.datetime.strptime(item, dt_format)


def main(data):
    guards = defaultdict(Counter)
    current_guard = None
    asleep = None

    for item in data:
        if 'begins' in item:
            current_guard = item.split()[3][1:]
        if 'falls' in item:
            asleep = extract_datetime(item.split(']')[0])
        if 'wakes' in item:
            awake = extract_datetime(item.split(']')[0])
            guards[current_guard] += Counter(range(asleep.minute, awake.minute))
    return guards


if __name__ == '__main__':
    results = main(get_data())
    guard = max(results.items(), key=lambda item: item[1].most_common(1)[0][1])
    print(int(guard[0]) * guard[1].most_common(1)[0][0])
