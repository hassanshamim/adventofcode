import itertools

from common import load_data


class Screen:
    def __init__(self, x, y):
        self.data = self.create_rectangle(x, y)

    def __iter__(self):
        return itertools.chain.from_iterable(self.data)

    def __str__(self):
        convert = lambda row: ''.join('#' if x else '.' for x in row)
        return '\n'.join(convert(row) for row in self.data)

    def rect(self, x, y):
        """
        rect AxB: turns on all of the pixels in a rectangle at the top-left
        of the screen which is A wide and B tall.
        """
        for row in self.data[:y]:
            row[:x] = [1] * x

    def rotate_row(self, idx, positions):
        """
        Rotate row y=A by B: shifts all of the pixels in row A (0 is the top row) right by B pixels.
        Pixels that would fall off the right end appear at the left end of the row.

        """
        row = self.data[idx]
        left, right = row[:-positions], row[-positions:]
        self.data[idx] = right + left

    def rotate_column(self, idx, positions):
        """
        rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels.
        Pixels that would fall off the bottom appear at the top of the column.
        """
        col = [row[idx] for row in self.data]
        top, bottom = col[:-positions], col[-positions:]
        col = bottom + top

        for row, newval in zip(self.data, col):
            row[idx] = newval

    @staticmethod
    def create_rectangle(x, y, default=0):
        """
        Creates an list of lists X by Y
        """
        return [[default for _ in range(x)] for _ in range(y)]

    def execute_instruction(self, text, dry_run=False):
        """
        Parses challenge instructions.  They take the following format:

        rect 1x1
        rotate row y=0 by 5
        rotate column x=30 by 1
        """
        text = text.split()
        if text[0] == 'rect':
            command = self.rect
            xy = text[-1]
            args = map(int, xy.split('x'))

        else:
            command = self.rotate_row if text[1] == 'row' else self.rotate_column
            positions = int(text[-1])
            idx = int(text[2].split('=')[-1])
            args = idx, positions

        if dry_run:
            return command, args

        command(*args)


def main():
    screen = Screen(50, 6)
    for line in load_data():
        screen.execute_instruction(line)
    print('Part 1: total pixels on:', sum(screen))
    # Part 2 is just reading the output
    print(screen)


if __name__ == '__main__':
    main()