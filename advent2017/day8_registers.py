from collections import defaultdict
from common import puzzle_input
import operator

PUZZLE_INPUT = puzzle_input(8)

operations = {
    '>': operator.gt,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
}
def part1(data=PUZZLE_INPUT):
    registers = defaultdict(int)
    for line in data:
        line = line.split()
        reg_char, command, amount, _if, *condition = line
        command = operator.add if command == 'inc' else operator.sub
        amount = int(amount)

        cond_reg, comparison, value = condition
        op = operations[comparison]
        if op(registers[cond_reg], int(value)):
            registers[reg_char] = command(registers[reg_char], amount)


        register = registers[reg_char]

    return max(registers.values())


def part2(data=PUZZLE_INPUT):
    registers = defaultdict(int)
    largest = 0
    for line in data:
        line = line.split()
        reg_char, command, amount, _if, *condition = line
        command = operator.add if command == 'inc' else operator.sub
        amount = int(amount)

        cond_reg, comparison, value = condition
        op = operations[comparison]
        if op(registers[cond_reg], int(value)):
            registers[reg_char] = command(registers[reg_char], amount)


        largest = largest if largest > max(registers.values()) else max(registers.values())

    return largest



    pass

if __name__ == '__main__':
    print('Part 1 result:', part1())
    print('Part 2 result:', part2())