from common import puzzle_input
from collections import Counter

from itertools import combinations


PUZZLE_INPUT = puzzle_input(2)

def edit_distance(s, t):
    "like levenshtein but only substitutions"
    return sum(c1 != c2 for c1, c2 in zip(s, t))


def exactly_two(text):
    return 2 in Counter(text).values()


def exactly_three(text):
    return 3 in Counter(text).values()


def part1(data=PUZZLE_INPUT):
    two_count = sum(exactly_two(s) for s in data)
    three_count = sum(exactly_three(s) for s in data)
    return two_count * three_count


def part2(data=PUZZLE_INPUT):
    for s1, s2 in combinations(data, 2):
        if edit_distance(s1, s2) == 1:
            return "".join(c1 if c1 == c2 else "" for c1, c2 in zip(s1, s2))


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 1:", part2())