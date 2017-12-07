from common import puzzle_input

PUZZLE_INPUT = [int(i) for i in puzzle_input(5)]


def part1(instructions=PUZZLE_INPUT):
    instructions = instructions.copy()
    lines_read = 0
    line = 0
    valid_lines = range(len(instructions))
    while line in valid_lines:
        lines_read += 1

        jump = instructions[line]
        instructions[line] += 1
        line += jump

    return lines_read

def part2(instructions=PUZZLE_INPUT):
    instructions = instructions.copy()
    lines_read = 0
    line = 0
    valid_lines = range(len(instructions))
    while line in valid_lines:
        lines_read += 1

        jump = instructions[line]
        instructions[line] += -1 if jump >= 3 else 1
        line += jump


    return lines_read


if __name__ == '__main__':
    example = [0, 3, 0, 1, -3]
    assert part1(example) == 5
    print('Part 1: number of jumps:', part1())

    assert part2(example) == 10

    print('Part 2: number of jumps:', part2())
