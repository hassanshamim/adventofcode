import itertools

from common import load_data


def extract_marker(data):
    marker = itertools.takewhile(lambda x: x != ')', data)
    marker = ''.join(marker)
    length, count = map(int, marker.split('x'))
    return length, count


def decompress(data):
    if iter(data) is data:
        it = data
    else:
        it = iter(data)

    return ''.join(_decompress(it))


def _decompress(data):
    for char in data:
        if char != '(':
            yield char
        else:
            length, repeat_count = extract_marker(data)
            marked_text = ''.join(itertools.islice(data, length))
            for _ in range(repeat_count):
                yield from marked_text


def decompress2(data):
    if iter(data) is data:
        it = data
    else:
        it = iter(data)

    return sum(i for i in _decompress2(it))


def _decompress2(data):
    for char in data:
        if char != '(':
            yield 1
        else:
            length, repeat_count = extract_marker(data)
            marked_text = ''.join(itertools.islice(data, length))
            for num in _decompress2(iter(marked_text)):
                yield repeat_count * num


def main1():
    data = joined_data()
    result = decompress(data)
    print('Length of decompressed data:', len(result))


def main2():
    data = joined_data()
    result = decompress2(data)
    print('Length of version 2 decompressed data:', result)


def joined_data():
    """ Treat list of lines as single string """
    return itertools.chain.from_iterable(load_data())


if __name__ == '__main__':
    main1()
    main2()
