# https://adventofcode.com/2018/day/1
from itertools import accumulate, cycle

from common import puzzle_input

PUZZLE_INPUT = [int(i) for i in puzzle_input(1)]


def seen_twice(iterable):
    seen = set()
    for element in iterable:
        if element in seen:
            yield element
        seen.add(element)


def part1(data=PUZZLE_INPUT):
    return sum(data)


def part2(data=PUZZLE_INPUT):
    return next(seen_twice(accumulate(cycle(data))))


if __name__ == "__main__":
    print("Part 1 result:", part1())
    print("Part 2 result:", part2())
