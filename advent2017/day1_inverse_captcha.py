from itertools import tee
from common import puzzle_input

PUZZLE_INPUT = puzzle_input(1)[0]


def circular_chunk(it: str):
    """
    yields it[0], it[1]: it[1], it[2]:, it[2], it[3]... it[n-2], it[n-1]
    as well as it[n-1], it[0]
    """
    a, b = tee(it)
    next(b)
    yield from zip(a, b)
    yield it[-1], it[0]


def halfway_chunk(it: str):
    """
    yields pairs of elements opposite from eachother
    """
    n = len(it)
    distance = n // 2
    for i in range(n):
        j = (i + distance) % n
        yield it[i], it[j]


def part1(data):
    chunks = circular_chunk(data)
    only_same = (int(a) for a, b in chunks if a == b)
    result = sum(only_same)
    return result


def part2(data):
    return sum(int(a) for a, b in halfway_chunk(data) if a == b)


if __name__ == '__main__':
    print('PART 1:', part1(PUZZLE_INPUT))
    print('PART 2:', part2(PUZZLE_INPUT))
