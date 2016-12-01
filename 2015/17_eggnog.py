#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:02:29 2016

@author: avendesora
"""

input_data = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

def permute(data, res=None, i=0):
    if res is None:
        res = []
    
    if i == len(data):
        yield res
    else:
        yield from permute(data, res=res+[data[i]], i=i+1)
        yield from permute(data, res=res, i=i+1)


def main1():
    target = 150

    valid_combos = sum(sum(containers) == target for containers in permute(input_data))
    print(valid_combos)

def main2():
    target = 150

    container_solution_count = {}
    for containers in permute(input_data):
        if sum(containers) == target:
            n = len(containers)
            container_solution_count.setdefault(n, 0)
            container_solution_count[n] += 1
    minimum_amount = min(container_solution_count.keys())
    print("{} combinations of {} containers".format(
          container_solution_count[minimum_amount], minimum_amount))
