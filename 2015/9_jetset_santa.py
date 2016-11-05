#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: hassanshamim
"""

import itertools


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_input():
    with open('./9_jetset_santa.txt', 'r') as file:
        for line in file.readlines():
            yield line.strip()


def parse(line):
    cities, distance = line.split(' = ')
    cities = cities.split(' to ')
    return cities, int(distance)


def create_lookup(data):
    lookup = {}
    for (start, stop), distance in data:
        lookup[(start, stop)] = lookup[(stop, start)] = distance
    return lookup


def route_distance(lookup_table, route):
    'takes a list of cities and returns the sum of distance between them, in order'
    city_combos = pairwise(route)
    return sum(lookup_table[cities] for cities in city_combos)


def main():
    # Build dict of distances
    data = [parse(line) for line in get_input()]
    distance_lookup = create_lookup(data)
    city_names = set(itertools.chain.from_iterable(distance_lookup.keys()))

    shortest = float('INFINITY')
    longest = 0
    # generate combinations of of possible paths
    all_possible_routes = itertools.permutations(city_names, len(city_names)) # 300k+ by my calculations

    # iterate over each path and find it's length
    for route in all_possible_routes:
        length = route_distance(distance_lookup, route)
        if length < shortest:
            shortest = length
        if length > longest:
            longest = length

    print('shortest combo is:', shortest, 'units')
    print('longest combo is:', longest, 'units')


if __name__ == '__main__':
    main()
