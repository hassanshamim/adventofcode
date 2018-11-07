from common import puzzle_input

from collections import defaultdict

PUZZLE_INPUT = puzzle_input(18)


class MusicBox:
    count = 0
    boxes = {}



    def __init__(self, instructions=PUZZLE_INPUT):
        self.instructions = instructions
        self.locked = False
        self.line_number = 0
        self.queue = []

        self.pid = MusicBox.count
        MusicBox.boxes[self.pid] = self
        MusicBox.count += 1

        self.registers = defaultdict(int)
        self.registers['p'] = self.pid

        self.tally = 0 # our part2 answer


    @property
    def other(self):
        other_pid = 1 - self.pid
        return self.boxes[other_pid]

    def run(self):
        line = self.instructions[self.line_number]

        cmd, *rest = line.split()
        if len(rest) == 1:
            a = rest[0]
        else:
            a, b, = rest
            b = self.registers[b] if b.isalpha() else int(b)

        if cmd == 'snd':
            a = self.registers[a] if a.isalpha() else int(a)
            self.other.queue.append(a)
            self.other.locked = False
            self.tally += 1
        elif cmd == 'rcv':
            if self.queue:
                self.locked = False
                val = self.queue.pop(0)
                self.registers[a] = val
            else:
                self.locked = True
                return
        elif cmd == 'set':
            self.registers[a] = b
        elif cmd == 'add':
            self.registers[a] += b
        elif cmd == 'mul':
            self.registers[a] *= b
        elif cmd == 'mod':
            self.registers[a] = self.registers[a] % b
        elif cmd == 'jgz':
            if self.registers[a] > 0:
                self.line_number += b
                return
        self.line_number += 1




def part1(data=PUZZLE_INPUT):
    registers = defaultdict(int)
    recovered = []
    jumps = 0
    played = None
    line_number = 0

    while True:
        line = data[line_number]

        cmd, *rest = line.split()
        if len(rest) == 1:
            a = rest[0]
        else:
            a, b, = rest
            b = registers[b] if b.isalpha() else int(b)

        if cmd == 'snd':
            played = registers[a]
        elif cmd == 'rcv':
            if registers[a] == 0:
                continue
            # recovered.append(played)
            return played
        elif cmd == 'set':
            registers[a] = b
        elif cmd == 'add':
            registers[a] += b
        elif cmd == 'mul':
            registers[a] *= b
        elif cmd == 'mod':
            registers[a] = registers[a] % b
        elif cmd == 'jgz':
            if registers[a] > 0:
                line_number += b
                continue
        line_number += 1


def part2(data=PUZZLE_INPUT):

    zero = MusicBox(instructions=data)
    one = MusicBox(instructions=data)

    assert zero.pid == 0
    assert one.pid == 1

    while True:
        if not one.locked:
            one.run()
        if not zero.locked:
            zero.run()

        if one.locked == zero.locked == True:
            return one.tally


example = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""".splitlines()

if __name__ == '__main__':
    print('part 1:', part1())
    #print('part 2:', part2())
