from common import find_data_file

from itertools import chain

def grouper(iterable, n):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEF', 3) --> ABC DEF"
    args = [iter(iterable)] * n
    return zip(*args)


def triangles_by_row():
    with open(find_data_file(), 'r') as f:
        for line in f:
            line = line.strip().split()
            yield map(int, line)


def triangles_by_column():
    '''group triangle sides by column, rather than row'''
    data = triangles_by_row()
    data = chain.from_iterable(zip(*data))
    yield from grouper(data, 3)


def count_valid(triangles):
    '''
    count valid triangles based on the three sides
    '''
    triangles = (sorted(sides) for sides in triangles)
    return sum(a + b > c for a, b, c in triangles)


if __name__ == '__main__':
    t1 = triangles_by_row()
    total_valid = count_valid(t1)
    print('Total valid triangles:', total_valid)

    t2 = triangles_by_column()
    total_valid = count_valid(t2)
    print('Total valid triangles(part2):', total_valid)
