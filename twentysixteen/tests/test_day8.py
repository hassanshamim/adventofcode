import pytest

from day8 import Screen


def test_examples():
    mini = Screen(7, 3)

    # all are 0 to start
    assert all(pixel is 0 for pixel in mini)

    mini.rect(3, 2)
    expected = '###....\n###....\n.......'

    assert str(mini) == expected

    mini.rotate_column(1, 1)
    expected2 = '#.#....\n###....\n.#.....'

    assert str(mini) == expected2

    mini.rotate_row(0, 4)
    expected3 = '....#.#\n###....\n.#.....'

    assert str(mini) == expected3

    mini.rotate_column(1, 1)
    expected4 = '.#..#.#\n#.#....\n.#.....'

    assert str(mini) == expected4



