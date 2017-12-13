from pathlib import Path
import re

from collections import UserList


def parse_int(line):
    return tuple(map(int, re.findall(r'\d+', line)))


def puzzle_input(day):
    input_file_name = f"day{day}_input.txt"
    day_input = Path(__file__).parent / 'puzzle_input' / input_file_name
    # assert day_input.exists(), f"Puzzle input {day_input} does not exist."

    return day_input.read_text().splitlines()


class CircularList(UserList):
    """" RIP IndexErrors """

    def __adjust(self, i): return i % len(self)

    def __getitem__(self, i):
        N = len(self)

        if isinstance(i, int):
            return self.data[i % N]

        elif isinstance(i, slice):
            # would this slice work as is?
            if bool(range(*i.indices(N))):
                return self.data[i]
            else:
                # very naive, not right
                new = slice(i.start % N, i.stop % N, i.step % N)
                return self.data[new]
        else:
            raise TypeError('Index must be int or slice.')

    def __setitem__(self, i, value):
        N = len(self)
        if isinstance(i, int):
            self.data[i % N] = value
        elif isinstance(i, slice):
            raise NotImplementedError
            # would this slice work as is?
            if bool(range(*i.indices(N))):
                return self.data[i]
            else:
                # very naive, not right
                new = slice(i.start % N, i.stop % N, i.step % N)
                return self.data[new]
        else:
            raise TypeError('Index must be int or slice.')

    def __delitem__(self, i):
        i = i % len(self)
        del self.data[i]

    def __iter__(self):
        return iter(self.data)
