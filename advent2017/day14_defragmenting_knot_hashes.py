from itertools import product

from common import puzzle_input
from day10_the_one_that_took_me_way_too_long import part2 as knot_hash

import networkx as nx

PUZZLE_INPUT = 'xlqgujun'


def hex2bin(chars):
    '''convert hex strings to binary strings'''
    as_int = [int(char, base=16) for char in chars]
    result = ''.join(bin(num)[2:].rjust(4, '0') for num in as_int)
    return result


def generate_grid(key):
    grid = []
    for i in range(128):
        newkey = key + '-' + str(i)

        result = knot_hash(newkey)
        result = hex2bin(result)
        grid.append(result)
    return grid


def part1(key=PUZZLE_INPUT):
    grid = generate_grid(key=key)
    return sum(row.count('1') for row in grid)


def part2(key=PUZZLE_INPUT):
    # with open('grid.txt') as f:
    #     grid = [line for line in f]
    grid = generate_grid(key=key)
    colsize, rowsize = len(grid[0]), len(grid)

    G = nx.Graph()

    for row, col in product(range(rowsize), range(colsize)):
        square = (row, col)
        if grid[row][col] == '1':
            G.add_node(square)
            adjacents = (row - 1, col), (row, col - 1)
            for row2, col2 in adjacents:
                if grid[row2][col2] == '1':
                    G.add_edge(square, (row2, col2))
    return sum(1 for group in nx.connected_components(G))


def test_examples():
    assert part2(key='flqrgnkx') == 1242
    assert hex2bin('0') == '0000'
    assert hex2bin('1') == '0001'


if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())