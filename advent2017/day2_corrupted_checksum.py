from itertools import combinations

from common import puzzle_input


def prepare(row: str):
    return [int(num) for num in row.split()]


def find_quotient(nums: list):
    for pair in combinations(sorted(nums, reverse=True), 2):
        result, remainder = divmod(*pair)
        if remainder == 0:
            return result


def part1(data=puzzle_input(2)):
    nums = [prepare(row) for row in data]
    result = sum(max(row) - min(row) for row in nums)
    return result


def part2(data=puzzle_input(2)):
    nums = [prepare(row) for row in data]
    result = sum(find_quotient(row) for row in nums)
    return result


if __name__ == '__main__':
    print('Part one result:', part1())
    print('Part 2:', part2())
