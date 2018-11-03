import math
from itertools import product
from typing import *
from common import puzzle_input


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


def parse_input():
    translations = {}
    for line in puzzle_input(21):
        before, after = line.split(" => ")
        translations[before] = Grid(after)

    return translations

PIXEL_ON = "#"
PIXEL_OFF = "."
PUZZLE_START = '.#./..#/###'


class Grid:
    def __init__(self, text: str) -> None:
        self.data = tuple(text.split("/"))  # keep it immutable

    def __len__(self) -> int:
        return len(self.data)

    def __reversed__(self) -> Iterator[str]:
        return reversed(self.data)

    def __getitem__(self, i: int) -> str:
        return self.data[i]

    def __str__(self) -> str:
        return "/".join(self.data)

    def __iter__(self) -> Iterator[str]:
        return iter(self.data)

    def rotate(self) -> "Grid":
        return Grid("/".join("".join(line) for line in zip(*reversed(self))))

    def flip(self) -> "Grid":
        return Grid("/".join(line[::-1] for line in self))

    @property
    def permutations(self) -> Iterable["Grid"]:
        rotations = 4
        flips = 2

        for num_rotations, num_flips in product(range(rotations), range(flips)):
            grid = self
            for _ in range(num_rotations):
                grid = grid.rotate()
            for _ in range(num_flips):
                grid = grid.flip()
            yield grid

    @classmethod
    def combine(cls, grids: List["Grid"]) -> "Grid":
        assert all(isinstance(obj, cls) for obj in grids)
        if len(grids) == 1:
            return grids[0]

        result = ""
        size = int(math.sqrt(len(grids)))
        for row_of_grids in chunks(grids, size):
            # append the grids' rows together
            rows = [''.join(row) for row in zip(*row_of_grids)]
            result += "/".join(rows)
            result += "/"

        return cls(result.rstrip("/"))

    def split(self) -> List["Grid"]:
        """
        Divide into NxN grids where N is 2 or 3.
        """
        if len(self) <= 3:
            return [self]
        if len(self) % 2 == 0:
            N = 2
        elif len(self) % 3 == 0:
            N = 3
        else:
            raise ValueError(f"Cannot split grid of size {len(self)}")

        result = []

        # group rows into chunks of N
        for nrows in chunks(self, N):
            # take first N chars from each row to make a new grid
            # ERROR HERE
            temp = [tuple(chunks(row, N)) for row in nrows]
            aligned = list(zip(*temp))
            new_grids = ['/'.join(segment) for segment in aligned]
            for grid in new_grids:
                result.append(Grid(grid))

            # for char_rows in zip(list(chunks(row, N)) for row in nrows):
            #     grid = Grid("/".join(char_rows))
            #     result.append(grid)

        return result


def part1(iterations=5):
    translations = parse_input()

    grids = [Grid(PUZZLE_START)]

    for i in range(iterations):
        # combine old subgrids
        grid = Grid.combine(grids)
        # split into new
        old_grids = grid.split()
        grids = []
        # transform new subgrids
        for item in old_grids:
            for permutation in item.permutations:
                if str(permutation) in translations:
                    grids.append(translations[str(permutation)])
                    break
            else: # no valid permutation found!
                raise ValueError(f'Cannot find matching translation for grid {str(item)}')

    # find how many are left on
    return sum(str(grid).count(PIXEL_ON) for grid in grids)





if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part1(18))
