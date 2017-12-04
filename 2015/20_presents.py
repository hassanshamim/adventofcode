# -*- coding: utf-8 -*-

from itertools import count, chain, repeat
from math import sqrt
import numpy as np


puzzle_input = 33100000 # presents


def find_house(target):
    """
    >>> find_house(13)
    8

    >>> find_house(6)
    4

    >>> find_house(4)
    3

    """
    for house in count(1):
        total_presents = calculate_presents(house) # sum multiples of house
        if total_presents >= target:
            # print('****RESULT: ', house)
            return house
        if house % 10000 == 0:
            print('count:', house)

def factors(n):
    upper_bound = int(sqrt(n)) + 1
    all_factors = ((i, n/i) for i in range(1, upper_bound) if not n%i)
    return set(chain.from_iterable(all_factors))



def calculate_presents(house_number):
    """
    >>> calculate_presents(9)
    13.0

    >>> calculate_presents(5)
    6.0
    """
    return sum(factors((house_number)))


def houses_to_visit(elf_num):
    """
    >>> houses_to_visit(3)
    (slice(2, 151, 3), 33)

    >>> houses_to_visit(5)
    (slice(4, 251, 5), 55)
    """
    start = elf_num - 1 # because we zero index
    stop = elf_num*50 + 1
    step = elf_num
    num_presents = elf_num * 11
    s = slice(start, stop, step)
    return s, num_presents


def main():
    target = puzzle_input / 10
    result = find_house(target)
    print('result', result)


def main2():
    houses = np.zeros(100000000) # hundred million
    target = puzzle_input

    for i in count(1):
        to_visit, amount = houses_to_visit(i)
        houses[to_visit] += amount

        if houses[i-1] >= target:
            print('Winner at house', i)
            break

        if i % 2000 == 0:
            print('visited house', i)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main2()
