from common import puzzle_input

PUZZLE_INPUT = [int(i) for i in puzzle_input(6)]

def cats(iterable):
    """concatenation"""
    return ''.join(map(str, iterable))


def part1(banks=PUZZLE_INPUT.copy()):
    seen = set()
    seen.add(cats(banks))
    cycles = 0

    while True:
        cycles += 1
        blocks = max(banks)
        biggest = banks.index(blocks)
        banks[biggest] = 0

        for idx in range(biggest+1, blocks+biggest+1):
            banks[idx % len(banks)] += 1

        if cats(banks) in seen:
            return cycles
        else:
            seen.add(cats(banks))


def part2(banks=PUZZLE_INPUT.copy()):
    seen = dict()
    cycles = 0
    seen[cats(banks)] = cycles

    while True:
        cycles += 1
        blocks = max(banks)
        biggest = banks.index(blocks)
        banks[biggest] = 0

        for idx in range(biggest+1, blocks+biggest+1):
            banks[idx % len(banks)] += 1

        if cats(banks) in seen:
            return cycles - seen[cats(banks)]
        else:
            seen[cats(banks)] = cycles

    # part 2, see how large the cycle is
    return part1(banks=banks)





if __name__ == '__main__':

    assert part1([0,2,7,0]) == 5
    assert part2([0,2,7,0]) == 4
    print('Part 1 number of cycles:', part1())
    print('Part 2 number of cycles:', part2())