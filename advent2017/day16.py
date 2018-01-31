from common import puzzle_input, parse_int

PUZZLE_INPUT = puzzle_input(16)[0].split(',')

def cat(args): return ''.join(args)


def part1(instructions=PUZZLE_INPUT, progs=None):
    if progs is None:
        progs = list('abcdefghijklmnop')

    for line in instructions:
        cmd = line.startswith
        if cmd('x'):
            a, b = parse_int(line)
            progs[b], progs[a] = progs[a], progs[b]
        elif cmd('p'):
            a, b = line[1], line[3]
            ai, bi = progs.index(a), progs.index(b)
            progs[ai], progs[bi] = progs[bi], progs[ai]
        elif cmd('s'):
            n = int(line[1:])
            progs = progs[-n:] + progs[:-n]
    

    return ''.join(progs)


def part2(instructions=PUZZLE_INPUT):
    count = 0
    seen = dict()
    progs = list('abcdefghijklmnop')
    while True:
        progs = part1(progs=list(progs))
        count += 1
        if progs in seen:
            break
        else:
            seen[progs] = count
    distance = count - seen[progs]
    remainder = (10**9 - seen[progs]) % distance
    for i in range(remainder):
        progs = part1(progs=list(progs))

    return progs


if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())
