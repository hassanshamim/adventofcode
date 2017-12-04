from itertools import tee

from ..day18 import generate_new_row, determine_tile_type


BIG_EXAMPLE = """.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^""".splitlines()


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def test_example():
    expected = "..^^. .^^^^ ^^..^".split()
    assert generate_new_row(expected[0]) == expected[1]
    assert generate_new_row(expected[1]) == expected[2]

def test_larger_example():
    for prev_row, next_row in pairwise(BIG_EXAMPLE):
        assert generate_new_row(prev_row) == next_row
