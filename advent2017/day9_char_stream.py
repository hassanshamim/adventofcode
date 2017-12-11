from common import puzzle_input
import sys

sys.setrecursionlimit(10000)  # BOOOOM

PUZZLE_INPUT = puzzle_input(9)[0]


def consume(stream, stop='>'):
    char = next(stream)
    while char != stop:
        if char == '!':
            next(stream)
        else:
            yield 1
        char = next(stream)


def group_score(stream, score=0):
    try:
        char = next(stream)
    except StopIteration:
        return 0
    if char == '<':
        list(consume(stream))
    elif char == '{':
        yield from group_score(stream, score=score + 1)
    elif char == '!':
        next(stream)
    elif char == '}':
        yield score
        yield from group_score(stream, score=score - 1)

    yield from group_score(stream, score=score)


def garbage_chars(stream):
    while True:
        try:
            char = next(stream)
        except StopIteration:
            return 0
        if char == '<':
            yield sum(consume(stream))
        elif char == '{':
            yield from garbage_chars(stream)
        elif char == '!':
            next(stream)


def part1(stream=PUZZLE_INPUT):
    s = iter(stream)
    totals = list(group_score(s))

    return sum(totals)


def part2(stream=PUZZLE_INPUT):
    s = iter(stream)
    totals = list(garbage_chars(s))

    return sum(totals)


def test_all_the_things():
    assert part1('{}') == 1
    assert part1('{{{}}}') == 6
    assert part1('{{},{}}') == 5
    assert part1('{{{},{},{{}}}}') == 16
    assert part1('{<a>,<a>,<a>,<a>}') == 1
    assert part1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert part1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert part1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

    assert part2('<>') == 0
    assert part2('<random characters>') == 17
    assert part2('<<<<>') == 3
    assert part2('<{!>}>') == 2
    assert part2('<!!>') == 0
    assert part2('<!!!>>') == 0
    assert part2('<{o"i!a,<{i<a>') == 10


if __name__ == '__main__':
    print('part 1 total: ', part1())
    print('part 2 total: ', part2())
    # 7100 too high
