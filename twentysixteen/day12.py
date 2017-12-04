from common import load_data
from string import digits

def parse(instruction):
    command, *args = instruction.split()
    args = tuple(int(arg) if arg[-1] in digits else arg for arg in args)

    return command, args


def execute(instructions, registers=None):
    if registers is None:
        registers = dict.fromkeys('abcd', 0)
    current_line = 0

    def inc(x): registers[x] += 1
    def dec(x): registers[x] -= 1
    def copy(x, y): registers[y] = registers[x] if x in registers else x
    def jump(x, num_lines):
        nonlocal current_line
        if registers.get(x, x) is not 0:
            current_line += num_lines - 1

    mapper = {'jnz': jump, 'cpy': copy, 'inc': inc, 'dec': dec}

    while current_line < len(instructions):
        command, args = parse(instructions[current_line])
        func = mapper[command]
        func(*args)
        current_line += 1

    return registers


def main1():
    instructions = [line for line in load_data()]
    registers = execute(instructions)
    result = registers['a']
    print("register a:", result)

def main2():
    # same as before but with register c starting at 1
    registers = dict.fromkeys('abd', 0)
    registers['c'] = 1

    instructions = [line for line in load_data()]
    registers = execute(instructions, registers)
    result = registers['a']
    print("register a:", result)


if __name__ == '__main__':
    # main1()
    main2()
