from functools import reduce
from operator import xor

puzzle_input = '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'
p1 = [int(num) for num in puzzle_input.split(',')]
p2 = [ord(c) for c in puzzle_input]


def ascii(s): return tuple(map(ord, s))


def part1(lengths=p1, n=256):

    data = list(range(n))

    current_position = skip_size = 0

    for length in lengths:
        r = range(current_position, current_position + length)
        section = [data[i % n] for i in r]
        for idx, num in zip(r, reversed(section)):
            data[idx % n] = num

        current_position += skip_size + length
        skip_size += 1

    return data[0] * data[1]


def part2(lengths=puzzle_input, n=256):
    lengths = list(map(ord, lengths))
    lengths.extend((17, 31, 73, 47, 23))
    data = list(range(n))

    current_position = skip_size = 0
    rounds = 64

    for _ in range(rounds):
        for length in lengths:
            r = range(current_position, current_position + length)
            section = [data[i % n] for i in r]
            for idx, num in zip(r, reversed(section)):
                data[idx % n] = num

            current_position += skip_size + length
            skip_size += 1

    dense_hash = [reduce(xor, data[i:i + 16]) for i in range(0, 256, 16)]

    def hexify(n): return hex(n)[2:].rjust(2, '0')
    return ''.join(map(hexify, dense_hash))


# def test_examples():
assert part1([3, 4, 1, 5], n=5) == 12
assert part2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert part2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert part2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    print('part 1 result:', part1())
    print('part 2 result:', part2())
