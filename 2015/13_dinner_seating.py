"""
In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along! This year, you resolve, will be different. You're going
to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness
would increase or decrease if they were to find themselves sitting next to each
other person. You have a circular table that will be just big enough to fit
everyone comfortably, and so each person will have exactly two neighbors.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""

import itertools
import re



regex = re.compile(r'^(\w+).*(gain|lose) (\d+) happiness units by sitting next to (\w+)\.')


def get_input():
    for line in open('day_13.input.txt', 'r').readlines():
        yield line.strip()


def parse(line):
    name, change, amount, neighbor =  regex.search(line).groups()
    amount = int(amount) if change == 'gain' else -int(amount)
    return name, neighbor, amount


def circular_double_pairwise(arrangement):
    '''
    >>>circular_pairwise([1, 2, 3])
    (1, 3), (3, 1), (1, 2), (2, 1), (2, 3), (3, 2)
    '''
    n = len(arrangement)  # Gotta be careful arrangement is not an iterator
    yield arrangement[0], arrangement[-1]
    yield arrangement[-1], arrangement[0]
    for i in range(n-1):
        yield arrangement[i], arrangement[i+1]
        yield arrangement[i+1], arrangement[i]


def score(seating_arrangement, lookup):
    return sum(lookup[pair] for pair in circular_double_pairwise(seating_arrangement))


def test():
    test_data = """Alice would gain 54 happiness units by sitting next to Bob.
    Alice would lose 79 happiness units by sitting next to Carol.
    Alice would lose 2 happiness units by sitting next to David.
    Bob would gain 83 happiness units by sitting next to Alice.
    Bob would lose 7 happiness units by sitting next to Carol.
    Bob would lose 63 happiness units by sitting next to David.
    Carol would lose 62 happiness units by sitting next to Alice.
    Carol would gain 60 happiness units by sitting next to Bob.
    Carol would gain 55 happiness units by sitting next to David.
    David would gain 46 happiness units by sitting next to Alice.
    David would lose 7 happiness units by sitting next to Bob.
    David would gain 41 happiness units by sitting next to Carol."""
    test_data = [line.strip() for line in test_data.splitlines()]

    relationships =  { (person, neighbor): amount for person, neighbor, amount
                                                  in map(parse, test_data)}
    guests = set(itertools.chain.from_iterable(relationships.keys()))
    possible_seating_arrangments = itertools.permutations(guests, len(guests))

    # delete later
    def get_score(val):
        return score(val, relationships)

    #best_score = max(score(arrangement, relationships) for arrangement in possible_seating_arrangments)
    best_score = max(possible_seating_arrangments, key=get_score)
    print('best score order for test example is:', best_score)
    print('best test score is:', get_score(best_score))



def main():
    print("PART 1")
    relationships =  { (person, neighbor): amount for person, neighbor, amount
                      in map(parse, get_input())}
    guests = set(itertools.chain.from_iterable(relationships.keys()))
    possible_seating_arrangments = itertools.permutations(guests, len(guests))

    best_score = max(score(arrangement, relationships) for arrangement in possible_seating_arrangments)
    print('best score is:', best_score)

    print("PART 2")
    me = 'me'
    for guest in guests:
        relationships[(me, guest)] = relationships[(guest, me)] = 0

    guests.add(me)
    possible_seating_arrangments = itertools.permutations(guests, len(guests))

    best_score = max(score(arrangement, relationships) for arrangement in possible_seating_arrangments)
    print('new best score is:', best_score)
    1/0





if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
    else:
        main()
