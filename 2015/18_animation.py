#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:35:48 2016

@author: avendesora
"""

test_data = [[False, True, False, True, False, True], [False, False, False, True, True, False], [True, False, False, False, False, True], [False, False, True, False, False, False], [True, False, True, False, False, True], [True, True, True, True, False, False]]

def fetch_data():
    """generator for input data"""
    with open('./day_18.input.txt', 'r') as f:
        for line in f.readlines():
            yield line.strip()


def create_grid():
    return [[True if c == '#' else False for c in line] for line in fetch_data()]


def print_grid(grid):
    for line in grid:
        print(''.join('#' if c is True else '.' for c in line))


def animate_grid(grid):
    ilen, jlen = len(grid), len(grid[0])
    next_grid = [[light_next_frame(grid, i, j) for j in range(ilen)] for i in range(jlen)]
    return next_grid


def light_next_frame(reference, i, j):
    current_state = reference[i][j]
    neighbors_on = sum(get_light(reference, coord) for coord in neighbors(i, j))
    if current_state:
        next_state = True if neighbors_on in (2, 3) else False
    else:
        next_state = True if neighbors_on == 3 else False
    return next_state


def neighbors(x, y):
    return [(x+1, y), (x, y+1), (x+1, y+1), (x-1, y), (x, y-1), (x-1, y-1),
            (x+1, y-1), (x-1, y+1)]


def get_light(lights, coord):
    i, j = coord
    
    # ignore negatives
    if i < 0 or j < 0:
        return False
    try:
        result = lights[i][j]
    except IndexError:
        result = False
    return result

    
def main1():
    grid = create_grid()
    num_steps = 100
    for i in range(num_steps):
        grid = animate_grid(grid)
    total = sum(sum(line) for line in grid)
    print('total lights on:', total)

def main2():
    def set_always_on(grid):
        max_i = len(grid)-1
        max_j = len(grid[0])-1
        grid[0][0] = grid[0][max_j] = grid[max_i][0] = grid[max_i][max_j] = True

    
    grid = create_grid()
    set_always_on(grid)
    num_steps = 100

    for i in range(num_steps):
        grid = animate_grid(grid)
        set_always_on(grid)

    total = sum(sum(line) for line in grid)
    print('total lights on:', total)
    
