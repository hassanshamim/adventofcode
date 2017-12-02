from itertools import combinations

from common import puzzle_input

PUZZLE_INPUT = [[int(num) for num in row.split()] for row in puzzle_input(2)]


def find_quotient(nums: list):
    for pair in combinations(sorted(nums, reverse=True), 2):
        result, remainder = divmod(*pair)
        if remainder == 0:
            return result


def part1(data=PUZZLE_INPUT):
    result = sum(max(row) - min(row) for row in data)
    return result


def part2(data=PUZZLE_INPUT):
    result = sum(find_quotient(row) for row in data)
    return result


if __name__ == '__main__':
    print('Part one result:', part1())
    print('Part 2:', part2())
