"https://adventofcode.com/2018/day/3"

from common import puzzle_input, parse_int

from collections import Counter


PUZZLE_INPUT = [parse_int(line) for line in puzzle_input(3)]


def square_inch_ids(x_offset, y_offset, width, height):
    """
    generates a series representing the ids each
    square inch of fabric used for this claim
    """
    start = y_offset * 1000 + x_offset
    for i in range(width):
        for j in range(height):
            yield start + i + (j * 1000)


def part1(data=PUZZLE_INPUT):
    square_count = Counter()

    for _id, *square in PUZZLE_INPUT:
        square_count.update(square_inch_ids(*square))

    return sum(count > 1 for count in square_count.values())


def part2(data=PUZZLE_INPUT):
    claim_ids = set()
    claimed_squares = {}
    for claim_id, *square in PUZZLE_INPUT:
        claim_ids.add(claim_id)

        for marked_square_inch in square_inch_ids(*square):
            other_square = claimed_squares.get(marked_square_inch)
            if (
                other_square is not None
            ):  # this square has already been claimed by another request
                other_square += (claim_id,)
                for sid in other_square:
                    claim_ids.discard(sid)
            else:
                other_square = (claim_id,)
                # it's not been claimed yet
            claimed_squares[marked_square_inch] = other_square

    assert len(claim_ids) == 1
    return claim_ids.pop()


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
