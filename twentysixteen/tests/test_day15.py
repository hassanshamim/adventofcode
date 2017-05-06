from ..day15 import make_disc_position_calculator, earliest_win


def test_provided_examples():
    """
    Disc #1 has 5 positions; at time=0, it is at position 4.
    Disc #2 has 2 positions; at time=0, it is at position 1
    """
    info = [(1, 5, 4), (2, 2, 1)]
    discs = []
    for args in info:
        discs.append(make_disc_position_calculator(*args))

    result = earliest_win(discs)
    assert result == 5
