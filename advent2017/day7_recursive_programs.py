from common import puzzle_input






class Node:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

def parse_line(line):
    if '->' in line:
        first, second = line.split('->')
        first = first.split()[0]
        second = second.strip().split(', ')

        return first, second
    else:
        return line.split()[0], []

PUZZLE_INPUT = [parse_line(line) for line in puzzle_input(7)]
def part1(data=PUZZLE_INPUT):
    has_children = set()
    is_child = set()

    for prog, children in PUZZLE_INPUT:
        if children:
            is_child = is_child.union(set(children))
            has_children.add(prog)


    for prog, _ in PUZZLE_INPUT:
        if (prog in has_children) and (prog not in is_child):
            return prog


def part2(data=PUZZLE_INPUT):
    """find the weight the incorrect disc *should* be"""

    # create node: children mapping:
    nodes = dict()
    for prog, children in PUZZLE_INPUT:
        nodes[prog] = children


    # start at root
    root = part1()
    # for each child, compare all weights


if __name__ == '__main__':
    print('part 1:', part1())


