from attr import attrs, attrib


@attrs
class Coord:
    x = attrib(default=0)
    y = attrib(default=0)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Can only add Coordinates to Coordinates, not {}'.format(type(other)))
        x = self.x + other.x
        y = self.y + other.y
        return Coord(x, y,)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('Can only multiply Coordinates by scalars not type {}'.format(type(other)))
        return Coord(self.x * other, self.y * other)


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


    def __abs__(self):
        return abs(self.position.x) + abs(self.position.y)

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

    def follow_instruction(self, instruction):

        turn, distance = instruction[:1], instruction[1:]
        self.change_direction(turn)
        traveled = self.calculate_travel_distance(distance)
        self.position += traveled


def calculate_taxi_distance(instructions):
    current = Person()
    for instruction in instructions:
        current.follow_instruction(instruction)

    return abs(current)

if __name__ == '__main__':
    with open('puzzle_input/day1_input.txt') as f:
        data = f.read().strip().split(', ')

    total_distance = calculate_taxi_distance(data)
    print('total distance:', total_distance)