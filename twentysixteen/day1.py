from itertools import repeat

from attr import attrs, attrib
from common import find_data_file


def smart_range(start, stop):
    step = 1 if start < stop else -1
    return range(start, stop, step)


@attrs
class Coord:
    x = attrib(default=0)
    y = attrib(default=0)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Can only add Coordinates to Coordinates, not {}'.format(type(other)))
        x = self.x + other.x
        y = self.y + other.y
        return Coord(x, y)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('Can only multiply Coordinates by scalars not type {}'.format(type(other)))
        return Coord(self.x * other, self.y * other)

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def path_to(self, other):
        """
        returns List of Coordinates in between self and other
        mimics `range` and includes starting position but not ending position

        Does not allow diagonal movement.
        """
        if not isinstance(other, self.__class__):
            raise TypeError('other must be type Coord not type {}'.format(type(other)))

        xs = smart_range(self.x, other.x) or repeat(self.x)
        ys = smart_range(self.y, other.y) or repeat(self.y)
        return [self.__class__(x, y) for x, y in zip(xs, ys)]
        # return [Coord(3,7), Coord(3,5)]



@attrs
class Person:
    DIRECTIONS = list('NESW')
    BASIS_VECTORS = {
        'N': Coord(0, 1),
        'E': Coord(1, 0),
        'W': Coord(-1, 0),
        'S': Coord(0, -1)
    }
    facing = attrib(default='N', validator=lambda obj, _, x: x in Person.DIRECTIONS)
    position = attrib(default=Coord())


    def change_direction(self, turn):
        """ Returns new cardinal direction after turning left or right """

        if turn not in 'LR':
            raise ValueError('Can only turn left and right (L or R)')

        direction = self.DIRECTIONS.index(self.facing)
        change = 1 if turn == 'R' else -1
        target = (direction + change) % len(self.DIRECTIONS)
        self.facing = self.DIRECTIONS[target]

    def calculate_travel_distance(self, distance):
        distance = int(distance)
        basis = self.BASIS_VECTORS[self.facing]
        return basis * distance

    @property
    def distance_from_origin(self):
        return abs(self.position)

    def follow_instruction(self, instruction):

        turn, distance = instruction[:1], instruction[1:]
        self.change_direction(turn)
        traveled = self.calculate_travel_distance(distance)
        self.position += traveled


def calculate_taxi_distance(instructions):
    """ Find distance of ending point from origin """
    current = Person()
    for instruction in instructions:
        current.follow_instruction(instruction)

    return current.distance_from_origin

def calculate_taxi_distance2(instructions): # Part 2
    """ Find distance of first revisited coordinate from origin """
    visited = set()
    current = Person()

    for instruction in instructions:
        old = current.position
        current.follow_instruction(instruction)
        new = current.position

        path_followed = old.path_to(new)
        for position in path_followed:
            if position in visited:
                return abs(position)
            visited.add(position)




if __name__ == '__main__':
    with open(find_data_file()) as f:
        data = f.read().strip().split(', ')

    total_distance = calculate_taxi_distance(data)
    print('total distance:', total_distance)

    # part 2
    total_distance2 = calculate_taxi_distance2(data)
    print('Distance to first repeated coordinate:', total_distance2)