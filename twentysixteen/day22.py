from collections import namedtuple
from itertools import permutations

from common import load_data

PUZZLE_DATA = list(load_data())[2:]

Node = namedtuple('Node', 'x y size used avail'.split())

def parse_line(line: str) -> Node:
    location, *stats, _ = line.split()
    _, x, y = location.split('-')
    x = int(x[1:])
    y = int(y[1:])
    size, used, avail = [int(stat[:-1]) for stat in stats]
    return Node(x, y, size, used, avail)


def valid(a: Node, b: Node) -> bool:
    return a != b and 0 < a.used < b.avail




def part1(data=PUZZLE_DATA):
    nodes = list(map(parse_line, data))
    pairs = permutations(nodes, 2)
    return sum(valid(*nodes) for nodes in pairs)


if __name__ == '__main__':
    print('part 1 result:', part1())
    # 627 too low