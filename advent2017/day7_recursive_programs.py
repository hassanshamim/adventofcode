from functools import lru_cache
from common import puzzle_input


class Node:
    NODES = dict()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Node.NODES[name] = self

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Node({self.name}, {self.weight})"

    @classmethod
    def get(cls, name):
        return cls.NODES[name]

def parse_line(line):
    if '->' in line:
        first, second = line.split('->')
        second = second.strip().split(', ')
    else:
        first = line
        second = []
    name, weight = first.strip().split()
    weight = int(weight.strip('()'))

    return Node(name, weight), second

PUZZLE_INPUT = [parse_line(line) for line in puzzle_input(7)]

def part1(data=PUZZLE_INPUT):
    has_children = set()
    is_child = set()

    for prog, children in data:
        if children:
            is_child = is_child.union(set(children))
            has_children.add(prog)


    for prog, _ in data:
        if (prog in has_children) and (prog.name not in is_child):
            return prog


def part2(data=PUZZLE_INPUT):
    """find the weight the incorrect disc *should* be"""

    # create node: children mapping:
    tree = dict()
    for prog, children in data:
        child_nodes = [Node.get(child) for child in children]
        tree[prog] = child_nodes


    @lru_cache(maxsize=None)
    def total_size(node):
        children = tree[node]
        return node.weight + sum(total_size(node) for node in children)


    for node, children in tree.items():
        if not children:
            continue

    # for each child, compare all weights
        weights = [total_size(child) for child in children]
    # if one differs from the rest
    # find the node whose total size corresponds to that weight
        if len(set(weights)) != 1:
            # find the odd one out
            odd_size = min(weights, key=weights.count)
            desired_size = max(weights, key=weights.count)
            odd_node = next(node for node in children if total_size(node) == odd_size)

            proper_node_weight = (desired_size - odd_size) + odd_node.weight
            print(proper_node_weight)
            # return proper_node_weight



if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())
    # 40299 too high, 'qwada'
    # 1181 too low
    # 1458 just right.  Fix code to get it first try
