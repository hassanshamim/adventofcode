from functools import wraps
import pytest
import re

from common import find_data_file

PARSERS = []


def all_int(x): return tuple(map(int, x))


def parse_with(matcher, cast=None):
    # playing with fire...
    def new_wrapper(original_func):
        @wraps(original_func)
        def inner_func(self, *args, **kwargs):
            if callable(cast):
                args = cast(args)
            return original_func(self, *args, **kwargs)

        inner_func.matcher = re.compile(matcher)
        PARSERS.append(inner_func)
        return inner_func
    # day = import_module('day21')
    return new_wrapper


class Scrambler:

    def __init__(self, start_password, reverse=False):
        self.pw = list(start_password)
        self.reverse = reverse

    @parse_with(r"swap position (\d+) with position (\d+)", cast=all_int)
    def swap_positions(self, i, j):
        """swap position 4 with position 0"""
        self.pw[i], self.pw[j] = self.pw[j], self.pw[i]

    @parse_with(r"swap letter (\w) with letter (\w)")
    def swap_letter(self, x, y):
        assert len(x) == len(y) == 1
        mapping = {x: y, y: x}
        self.pw = [mapping.get(char, char) for char in self.pw]

    @parse_with(r"rotate (\w+) (\d+) step", cast=lambda group: (group[0], int(group[1])))
    def rotate(self, direction, n):
        assert direction in ['left', 'right'], f"bad direction {direction}"

        n = n if direction == 'left' else -n
        if self.reverse:
            n = -n
        self.pw = self.pw[n:] + self.pw[:n]

    @parse_with(r"rotate based on position of letter (\w)")
    def rotate_on_char(self, char):
        idx = self.pw.index(char)
        if self.reverse:
            # mapping of new index to number of rotations to get back to its original position

            positions = {0: 1, 1: 0, 2: 8, 3: 1, 4: 11, 5: 2, 6: 6, 7: 3}
            # positions = {0: 1, 1: 7, 2: 8, 3: 1, 4: 11, 5: 2, 6: 6, 7: 3}
            num_rotations = positions[idx] - idx
            # num_rotations = positions[idx]

            if num_rotations < 0:
                num_rotations = 8 - num_rotations
        else:
            num_rotations = idx + 1 if idx < 4 else idx + 2
        for _ in range(num_rotations):
            self.rotate('right', 1)

    @parse_with(r"reverse positions (\d+) through (\d+)", cast=all_int)
    def reverse_positions(self, i, j):
        middle_reversed = list(reversed(self.pw[i:j + 1]))
        self.pw = self.pw[:i] + middle_reversed + self.pw[j + 1:]

    @parse_with(r"move position (\d+) to position (\d)", cast=all_int)
    def move_position(self, i, j):
        if self.reverse:
            i, j = j, i
        char = self.pw.pop(i)
        self.pw.insert(j, char)

    def parse(self, line, debug=False):
        for func in PARSERS:
            if func.matcher.match(line):
                args = func.matcher.match(line).groups()
                if debug:
                    print('calling function', func.__name__,
                          'with arguments: ', *args)
                    # text = f"calling {func.__name__}({','.join(*args)})"
                return func(self, *args)


def main1():
    starting_pw = 'abcdefgh'
    scram = Scrambler(starting_pw)

    with open(find_data_file()) as f:
        for line in f:
            scram.parse(line)

    print('PART 1 RESULT:', ''.join(scram.pw))


def main2():
    ending_pw = 'fbgdceah'
    scram = Scrambler(ending_pw, reverse=True)

    with open(find_data_file()) as f:
        for line in reversed(f.readlines()):
            scram.parse(line)

    # abdfcgeh WRONG
    # hdegabfc WRONG
    print('PART 2 RESULT:', ''.join(scram.pw))


if __name__ == '__main__':
    main1()
    main2()


def test_example():
    scram = Scrambler('abcde')

    scram.swap_positions(4, 0)
    assert scram.pw == list('ebcda')

    scram.swap_letter('d', 'b')
    assert scram.pw == list('edcba')

    scram.reverse_positions(0, 4)
    assert scram.pw == list('abcde')

    scram.rotate('left', 1)
    assert scram.pw == list('bcdea')

    scram.move_position(1, 4)
    assert scram.pw == list('bdeac')

    scram.move_position(3, 0)
    assert scram.pw == list('abdec')

    scram.rotate_on_char('b')
    assert scram.pw == list('ecabd')

    scram.rotate_on_char('d')
    assert scram.pw == list('decab')


def test_parse_example():
    scram = Scrambler('abcde')

    scram.parse('swap position 4 with position 0')
    assert scram.pw == list('ebcda')

    scram.parse('swap letter d with letter b')
    assert scram.pw == list('edcba')

    scram.parse('reverse positions 0 through 4')
    assert scram.pw == list('abcde')

    scram.parse('rotate left 1 step')
    assert scram.pw == list('bcdea')

    scram.parse('move position 1 to position 4')
    assert scram.pw == list('bdeac')

    scram.parse('move position 3 to position 0')
    assert scram.pw == list('abdec')

    scram.parse('rotate based on position of letter b')
    assert scram.pw == list('ecabd')

    scram.parse('rotate based on position of letter d')
    assert scram.pw == list('decab')


@pytest.fixture
def pw():
    yield list('01234567')


@pytest.fixture
def scram(pw):
    yield Scrambler(pw)


def test_unscrable_move_position(pw, scram):
    scram.move_position(1, 4)
    undo = Scrambler(scram.pw, reverse=True)
    undo.move_position(1, 4)
    assert undo.pw == pw


def test_unscrable_swap_positions(pw, scram):
    scram.swap_positions(2, 6)

    undo = Scrambler(scram.pw, reverse=True)
    undo.swap_positions(2, 6)
    assert undo.pw == pw


def test_unscrable_swap_letters(pw, scram):
    scram.swap_letter('4', '0')

    undo = Scrambler(scram.pw, reverse=True)
    undo.swap_letter('4', '0')
    assert undo.pw == pw


def test_unscrable_reverse_positions(pw, scram):
    scram.reverse_positions(3, 7)
    undo = Scrambler(scram.pw, reverse=True)
    undo.reverse_positions(3, 7)
    assert undo.pw == pw


directions = ['left', 'right']
rotations = range(1, 9)
from itertools import product
combos = list(product(directions, rotations))


@pytest.mark.parametrize('direction,i', combos)
def test_unscrable_rotate(pw, scram, direction, i):
    scram.rotate(direction, i)

    undo = Scrambler(scram.pw, reverse=True)
    undo.rotate(direction, i)
    assert undo.pw == pw


@pytest.mark.parametrize('char', list('01234567'))
def test_unscrable_rotate_on_char(scram, pw, char):
    scram.rotate_on_char(char)

    undo = Scrambler(scram.pw, reverse=True)
    undo.rotate_on_char(char)

    assert undo.pw == pw
