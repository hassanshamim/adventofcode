PUZZLE_INPUT = 347991


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


if __name__ == '__main__':  # Examples
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31
    print('part 1 result:', part1())
