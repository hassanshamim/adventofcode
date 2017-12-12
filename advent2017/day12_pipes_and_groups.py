from common import puzzle_input


def parse_input(data=puzzle_input(12)):
    for line in data:
        left, right = line.split(' <-> ')
        right = set(map(int, right.split(',')))
        yield int(left), right

PUZZLE_INPUT = dict(parse_input())


def part1(data=PUZZLE_INPUT):
    to_visit = {0}
    seen = set()

    while to_visit:
        i = to_visit.pop()
        seen.add(i)
        to_visit.update(data[i] - seen)

    return len(seen)

def part2(data=PUZZLE_INPUT):
    data = data.copy()
    groups = 0

    while data:  # while there are nodes that havent been seen
        seed = next(iter(data))

        to_visit = {seed}
        seen = set()
        # as long as there are unvisited nodes in the group
        while to_visit:
            i = to_visit.pop()
            to_visit.update(data[i] - seen)
            seen.add(i)
        else: # increment and cleanup
            groups += 1
            for item in seen:
                del data[item]
    return groups


if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())
