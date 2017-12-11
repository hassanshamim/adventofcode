from common import puzzle_input

PUZZLE_INPUT = puzzle_input(11)[0].split(',')

Coord = complex

DIRECTIONS = {
    'n': Coord(0, -1),
    'ne': Coord(1, -1),
    'se': Coord(1, 0),
    's': Coord(0, 1),
    'sw': Coord(-1, 1),
    'nw': Coord(-1, 0),
}


def distance(a, b):
    # Use cube distance algorithm, must convert to 3 basis vectors first
    x1, x2 = a.real, b.real
    z1, z2 = a.imag, b.imag
    y1, y2 = (-x1 - z1), (-x2 - z2)

    return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) // 2


def part1(data=PUZZLE_INPUT):

    start = Coord(0, 0)
    for direction in data:
        start += DIRECTIONS[direction]

    return distance(Coord(0, 0), start)


def part2(data=PUZZLE_INPUT):
    top = 0
    start = Coord(0, 0)
    for direction in data:
        start += DIRECTIONS[direction]
        dist = distance(Coord(0, 0), start)
        if dist > top:
            top = dist

    return top


if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())
