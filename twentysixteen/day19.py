"""
Silly elves play white elephant all wrong.
"""

import numpy as np
PUZZLE_INPUT = 3017957
from collections import deque


# from line_profiler import LineProfiler

# def do_profile(follow=[]):
#     def inner(func):
#         def profiled_func(*args, **kwargs):
#             try:
#                 profiler = LineProfiler()
#                 profiler.add_function(func)
#                 for f in follow:
#                     profiler.add_function(f)
#                 profiler.enable_by_count()
#                 return func(*args, **kwargs)
#             finally:
#                 profiler.print_stats()
#         return profiled_func
#     return inner

def main1_first(size):
    """
    Too slow given the input size but good example of function composition.
    """
    from intertools import cycle
    elves_in_circle = np.ones(size)
    elves_with_indexes = enumerate(np.ones())
    repeating_elves = cycle(elves_with_indexes)
    remaining_elves_with_indexes = filter(lambda idx, still_alive: still_alive, repeating_elves) 

    def pairwise(it):
        """
        consume the iterable two items at a time
        """
        yield next(it), next(it)

    # main algorithm
    for turn, neighbor in pairwise(remaining_elves):
        # if only one elf left, they are the winner
        if turn == neighbor:
            print(turn[0], 'elf wins!')
            break
        # else, the neighbor is knocked out
        else:
            elves_in_circle[neigbor[0]] = 0



    

def main1():
    remaining_elves = np.arange(1, PUZZLE_INPUT+1)

    while len(remaining_elves) != 1:
        win_this_round = np.delete(remaining_elves, slice(1, None, 2))
        # Move last person to front if they didn't steal their neighbors
        if remaining_elves.size % 2 == 1:
            win_this_round = np.roll(win_this_round, 1)
        remaining_elves = win_this_round

    print(f"Winning elf is: {remaining_elves[0]}")


# @do_profile
def main2():
    """
    Now they steal the presents of the person across from them
    (and to the left if it's a tie).
    """
    # PUZZLE_INPUT = 5
    split_at = PUZZLE_INPUT // 2

    # Create two deques, each representing half of the circle
    first_half = deque(range(1, split_at+1))
    second_half = deque(range(split_at+1, PUZZLE_INPUT+1))

    # as long as there isn't a winner
    while first_half and second_half:
        # remove the loser
        second_half.popleft()

        # 'rotate' so whoever is up next is at the front
        # While keeping second half equal to or larger the second
        if len(first_half) == len(second_half):
            first_half.append(second_half.popleft())

        second_half.append(first_half.popleft())

    winner = (first_half or second_half)[0]
    # only winner is left
    print('Round 2 winner:', winner)


if __name__ == '__main__':
    # main1()
    main2()
