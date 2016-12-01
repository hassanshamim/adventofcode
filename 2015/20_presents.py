# -*- coding: utf-8 -*-

puzzle_input = 33100000 # presents
from itertools import count, chain
from math import sqrt


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
    13
    >>> calculate_presents(5)
    6
    """
    return sum(factors((house_number)))


def main():
    target = puzzle_input / 10
    result = find_house(target)
    print('result', result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
