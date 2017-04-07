from collections import namedtuple, deque
from itertools import combinations, chain

RTGPairOrig = namedtuple('RTGPair', ['chip', 'gen'])
NUM_FLOORS = 4

class RTGPair:
    """
    Like a named tuple but with some convenience methods
    """
    __slots__ = ('chip', 'gen')

    def __init__(self, chip, gen):
        self.chip = chip
        self.gen = gen

    def __repr__(self):
        return "<RTGPair({}, {})>".format(self.chip, self.gen)

    def __hash__(self):
        return hash((self.chip, self.gen))

    def __iter__(self):
        yield self.chip
        yield self.gen

    def _replace(self, name, value):
        """
        Return new RTG object with updated value.
        """
        if name == 'chip':
            return self.__class__(value, self.gen)
        else:
            return self.__class__(self.chip, value)

    def increment(self, attr):
        return self._replace(attr, getattr(self, attr) + 1)

    def decrement(self, attr):
        return self._replace(attr, getattr(self, attr) - 1)


class GameState:
    def __init__(self, elevator, pairs):
        self.elevator = elevator
        self.rtgs = [RTGPair(chip, gen) for chip, gen in pairs]

    def __iter__(self):
        return iter(self.as_tuple())

    def __repr__(self):
        elev, *rtgs = self.as_tuple()
        return "<GameState({}, {})".format(elev, rtgs)

    def __hash__(self):
        # needs to be tuple so its hashable
        return hash(self.as_tuple())

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def as_tuple(self):
        return (self.elevator, ) + tuple((chip, gen)
                                         for chip, gen in self.rtgs)

    def values(self):
        yield self.elevator
        yield from chain.from_iterable(self.rtgs)

    @property
    def generators(self):
        return [rtg.gen for rtg in self.rtgs]

    @property
    def chips(self):
        return [rtg.chip for rtg in self.rtgs]

    @classmethod
    def floor_valid(cls, piece):
        return 1 <= piece <= NUM_FLOORS

    @property
    def valid(self):
        """
        state is invalid if any chip is on the same floor as a generator
        without it's own generator

        Also check floors are within bounds - doing that here rather than neigbhor state generator
        """
        gens = set(self.generators)
        pieces_on_valid_floors = all(1 <= piece <= NUM_FLOORS for piece in self.values())
        no_fried_chips = all(rtg.chip == rtg.gen or rtg.chip not in gens
                             for rtg in self.rtgs)

        return no_fried_chips and pieces_on_valid_floors

    def replace(self, pieces, adjustment):
        """
        Returns a new GameState with rtg pieces and elevator + adjustment
        pieces in format [(1, 'gen'), (3, 'chip') ...]
        adjustment is either 1 or -1
        """
        elevator = self.elevator + adjustment
        rtgs = self.rtgs[:]
        adjust = RTGPair.increment if adjustment == 1 else RTGPair.decrement
        for idx, piece in pieces:
            rtg = rtgs[idx]
            rtgs[idx] = adjust(rtg, piece)
        return self.__class__(elevator, rtgs)

    def neighbor_states(self):
        """
        generator to return possible states by moving
        pieces up or down a level based on current location of elevator.
        """
        available = []  # rtg pieces on current floor
        for i, rtg in enumerate(self.rtgs):
            for field in 'chip', 'gen':
                if getattr(rtg, field) == self.elevator:
                    available.append((i, field))

        for move in available:
            yield self.replace([move], 1)
            yield self.replace([move], -1)

        for moves in combinations(available, 2):
            yield self.replace(moves, 1)
            yield self.replace(moves, -1)

    def valid_neighbor_states(self):
        for state in self.neighbor_states():
            if state.valid:
                yield state


puzzle_input = GameState(
    1,  #elevator
    [ # Chip, Gen
        (2, 1),  # Polonium
        (1, 1),  # Thulium
        (2, 1),  # Promethium
        (1, 1),  # ruthenium
        (1, 1),  # cobalt
    ]
)

GOAL = GameState(
    4,
    [
        (4, 4),  # Polonium
        (4, 4),  # Thulium
        (4, 4),  # Promethium
        (4, 4),  # ruthenium
        (4, 4),  # cobalt
    ])
NUM_FLOORS = 4



def BFS(state, verbose=False):
    depth = -1
    next_level = deque()
    next_level.append(state)
    visited = set()

    while True:
        current_level, next_level = next_level, deque()
        depth += 1
        if verbose:
            print('------------------------')
            print('starting level', depth)
            print('------------------------')

        while current_level:
            state = current_level.popleft()

            if state == GOAL:
                return depth
            if hash(state) not in visited:
                next_level.extend(state.valid_neighbor_states())
                visited.add(hash(state))
                if verbose:
                    print('now have seen', len(visited), 'gamestates')


def main1():
    current = puzzle_input
    smallest = BFS(current, verbose=True)
    print('minimum steps to goal:', smallest)


if __name__ == '__main__':
    main1()
'''
Can encode data like: [Elevfloor, (gen1floor, chip1floor), (gen2floor, chip2loor) ]
Ideal state: [4, (4,4),(4,4)] etc
The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant.
'''
