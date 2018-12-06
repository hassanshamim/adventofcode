from itertools import product, repeat
from string import ascii_letters

from common import parse_int, puzzle_input

PUZZLE_INPUT = [parse_int(line) for line in puzzle_input(6)]
WIDTH = 360


def distance(x, y):
    """manhatten distance"""
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def closest(coord, candidates):
    distances = sorted(
        [(distance(coord, candidate), candidate) for candidate in candidates],
        key=lambda result: result[0],
    )
    # check if it's equidistant
    if distances[0][0] == distances[1][0]:
        return None
    else:
        return distances[0][1]


def part1(data=PUZZLE_INPUT):
    region_sizes = dict.fromkeys(data, 0)
    infinite_regions = set()

    edges = [
        zip(range(WIDTH), repeat(0)),  # TOP
        zip(repeat(0), range(0, WIDTH)),  # LEFT
        zip(repeat(WIDTH - 1), range(WIDTH - 1, WIDTH * WIDTH, WIDTH)),  # RIGHT
        zip(range(WIDTH), repeat(WIDTH - 1)),  # BOTTOM
    ]

    for edge in edges:
        for node in edge:
            infinite_region = closest(node, data)
            if infinite_region is not None:
                infinite_regions.add(infinite_region)

    for node in product(range(WIDTH), repeat=2):
        region = closest(node, data)
        if region is not None:
            region_sizes[region] += 1

    # return size of largest area that isn't infinite
    non_infinite = region_sizes.keys() - infinite_regions
    return max(region_sizes[region] for region in non_infinite)


def test_example_part1():
    example = """1, 1
                1, 6
                8, 3
                3, 4
                5, 5
                8, 9""".splitlines()
    example = [parse_int(line) for line in example]
    result = part1(data=example)
    assert result == 17


def part2(data=PUZZLE_INPUT):
    MAX_DISTANCE = 10000
    region_count = 0
    for node in product(range(WIDTH), repeat=2):
        total_distances = sum(distance(node, coord) for coord in data)
        if total_distances < MAX_DISTANCE:
            region_count += 1
    return region_count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
