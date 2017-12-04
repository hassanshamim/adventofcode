from collections import namedtuple, deque
from itertools import combinations, chain


class RTGPair(namedtuple('RTGPair', 'chip gen')):
    """
    Like a named tuple but with some convenience methods
    """
    __slots__ = ()

    def increment(self, attr):
        return self._replace(**{attr: getattr(self, attr) + 1})

    def decrement(self, attr):
        return self._replace(**{attr: getattr(self, attr) - 1})


class GameState(namedtuple('GameState', 'elevator rtgs')):
    """
    Again a namedtuple with some methods for finding neighboring states
    """
    __slots__ = ()
    NUM_FLOORS = 4

    def __new__(cls, elevator, pairs):
        rtgs = tuple(RTGPair(*pair) for pair in pairs)
        self = super().__new__(cls, elevator, rtgs)
        return self

    def __hash__(self):
        """
        position of pairs is all that matters, not which pairs are where
        So we sort before hashing to reduce possible gamestates space.
        May not matter when we move to priority queue.
        """
        return hash((self.elevator, ) + tuple(sorted(self.rtgs)))

    @property
    def valid(self):
        """
        state is invalid if any chip is on the same floor as a generator
        without it's own generator

        Also check floors are within bounds - doing that here rather than neigbhor state generator
        """
        floors_with_generators = set(rtg.gen for rtg in self.rtgs)
        pieces_on_valid_floors = all(1 <= piece <= self.NUM_FLOORS
                                     for piece in self.values())
        no_fried_chips = all(rtg.chip == rtg.gen or
                             rtg.chip not in floors_with_generators
                             for rtg in self.rtgs)

        return no_fried_chips and pieces_on_valid_floors

    def values(self):
        yield self.elevator
        yield from chain(*self.rtgs)

    def replace(self, pieces, adjustment):
        """
        Returns a new GameState with rtg pieces and elevator + adjustment
        pieces in format [(1, 'gen'), (3, 'chip') ...]
        adjustment is either 1 or -1
        """
        elevator = self.elevator + adjustment
        rtgs = list(self.rtgs)
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


def BFS(start, goal, verbose=False):
    """
    We want the minimum steps, so breadth-first it is
    """
    depth = -1
    next_level = deque()
    next_level.append(start)
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

            if state == goal:
                return depth
            if hash(state) not in visited:
                visited.add(hash(state))
                next_level.extend(state.valid_neighbor_states())
                if verbose:
                    print('now have seen', len(visited), 'gamestates')


puzzle_input1 = GameState(
    1,  #elevator
    [ # Chip, Gen
        (2, 1),  # Polonium
        (1, 1),  # Thulium
        (2, 1),  # Promethium
        (1, 1),  # ruthenium
        (1, 1),  # cobalt
    ]
)
puzzle_input2 = GameState(
    1,  #elevator
    [ # Chip, Gen
        (2, 1),  # Polonium
        (1, 1),  # Thulium
        (2, 1),  # Promethium
        (1, 1),  # ruthenium
        (1, 1),  # cobalt
        (1, 1),  # Part 2
        (1, 1),  # Part 2
    ]
)

GOAL1 = GameState(
    4,
    [
        (4, 4),  # Polonium
        (4, 4),  # Thulium
        (4, 4),  # Promethium
        (4, 4),  # ruthenium
        (4, 4),  # cobalt
    ])
GOAL2 = GameState(
    4,
    [
        (4, 4),  # Polonium
        (4, 4),  # Thulium
        (4, 4),  # Promethium
        (4, 4),  # ruthenium
        (4, 4),  # cobalt
        (4, 4),  # Part 2
        (4, 4),  # Part 2
    ])


def main1():
    """
    Result from BFS:
    ------------------------
    starting level 47
    now have seen 158161 gamestates
    now have seen 158162 gamestates
    minimum steps to goal: 47

    BFS with sort before hashing:
    ------------------------
    starting level 47
    now have seen 4331 gamestates
    minimum steps to goal: 47
    """
    smallest = BFS(puzzle_input1, GOAL1, verbose=True)
    print('minimum steps to goal:', smallest)


def main2():
    smallest = BFS(puzzle_input2, GOAL2, verbose=True)

    print('Part 2:')
    print('minimum steps to goal:', smallest)


if __name__ == '__main__':
    main1()
    # main2()