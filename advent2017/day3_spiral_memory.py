from itertools import cycle, product

PUZZLE_INPUT = 347991

Coord = complex


def find_ring(n):
    """Finds the base x base ring in which n resides"""
    base = 1
    while base**2 < n:
        base += 2
    return base


def ring_perimeter(n):
    """finds total length of perimeter of nxn ring in block size"""
    return 2 * n + 2 * (n - 2)


def part1(num=PUZZLE_INPUT):
    """
    finds distance to the center by calculating ring size as well as finding
    the distance of `num` from the center of its respective column/row
    """
    if num == 1:  # edge case
        return 0

    ring = find_ring(num)
    perim = ring_perimeter(ring)

    # simulate indexing the ring at 0
    idx = num - (ring - 2)**2

    # collapse onto a single side
    side_length = perim // 4
    idx = idx % side_length

    # find distance of num from center
    center_block = side_length // 2
    distance = abs(idx - center_block)

    return (ring // 2) + distance


def spiral_coords():
    """
    Generator of coordinates in spiral starting from origin (0,0)
    """
    LEFT = Coord(-1, 0)
    RIGHT = Coord(1, 0)
    UP = Coord(0, 1)
    DOWN = Coord(0, -1)

    current = Coord(0, 0)
    steps = 1

    yield current

    for group in cycle([[RIGHT, UP], [LEFT, DOWN]]):
        for direction in group:
            for i in range(steps):
                current += direction
                yield current
        steps += 1


def neighbors(coord):
    return {coord + Coord(*xy) for xy in product([-1, 0, 1], repeat=2)}


def part2(num=PUZZLE_INPUT):
    """Just straight up builds the spiral because I don't see any better ways"""
    # loop through spiral
    #   sum neighbors in seen or set val to 1
    #   add coord to seen
    #   stop if value is > num
    seen = dict()
    spiral = spiral_coords()
    seen[next(spiral)] = 1
    for coord in spiral:
        value = sum(seen.get(adjacent, 0) for adjacent in neighbors(coord))
        seen[coord] = value
        if value > num:
            return value


if __name__ == '__main__':  # Examples
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31
    print('part 1 result:', part1())

    print('part2 results:', part2())
