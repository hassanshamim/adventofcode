from collections import Counter
from itertools import combinations

from common import puzzle_input

PUZZLE_INPUT = puzzle_input(2)


def edit_distance(w1, w2):
    "like levenshtein but only substitutions"
    return sum(char1 != char2 for char1, char2 in zip(w1, w2))


def exactly_two(text):
    return 2 in Counter(text).values()


def exactly_three(text):
    return 3 in Counter(text).values()


def part1(data=PUZZLE_INPUT):
    two_count = sum(exactly_two(word) for word in data)
    three_count = sum(exactly_three(word) for word in data)
    return two_count * three_count


def part2(data=PUZZLE_INPUT):
    for word1, word2 in combinations(data, 2):
        if edit_distance(word1, word2) == 1:
            return "".join(c1 if c1 == c2 else "" for c1, c2 in zip(word1, word2))


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 1:", part2())
