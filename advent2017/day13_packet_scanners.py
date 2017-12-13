from common import puzzle_input, parse_int

PUZZLE_INPUT = dict(map(parse_int, puzzle_input(13)))


def scanner_on_top(rnge, turn=0):
    if rnge == 0:
        return False
    trip_time = (rnge - 1) * 2
    if turn >= trip_time:
        return turn % trip_time == 0
    else:
        return turn == 0


def part1(data=PUZZLE_INPUT):
    return sum(depth * range for depth, range in data.items()
               if scanner_on_top(range, depth))


def part2(data=PUZZLE_INPUT):
    delay = 1
    while True:
        if not any(
                scanner_on_top(rnge, depth + delay)
                for depth, rnge in data.items()):
            return delay
        else:
            delay += 1


if __name__ == '__main__':
    example = {0: 3, 1: 2, 4: 4, 6: 4}
    assert part1(example) == 24
    assert part2(data=example) == 10
    print('part 1:', part1())
    print('part 2:', part2())
