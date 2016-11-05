#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 00:50:41 2016

@author: Hassan Shamim

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""
from collections import defaultdict
from itertools import zip_longest

data_file = './day_3.input'

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def count_unique(data):
    counter = defaultdict(int)
    current_position = (0, 0)
    counter[current_position] += 1
    directions = {'^': lambda x, y: (x, y+1),
                   '>': lambda x, y: (x+1, y),
                   '<': lambda x, y: (x-1, y),
                   'v': lambda x, y: (x, y-1)
                   }
    for direction in data:
        current_position = directions[direction](*current_position)
        counter[current_position] += 1
        
    print('total houses visited', len(counter))
    
def count_with_robo_santa(data):
    counter = set((0, 0))
    santa, robo_santa = (0,0), (0,0)
    directions = { '^': lambda x, y: (x, y+1),
                   '>': lambda x, y: (x+1, y),
                   '<': lambda x, y: (x-1, y),
                   'v': lambda x, y: (x, y-1),
                   }
    for santa_dir, rs_dir in grouper(data, 2):
        santa = directions[santa_dir](*santa)
        robo_santa = directions[rs_dir](*robo_santa)
        counter.update({robo_santa, santa})
    print('total houses robo and regular santa visited:', len(counter))
    
    
    
with open(data_file) as f:
    data = f.read()
    count_unique(data)
    count_with_robo_santa(data)