import pytest

from twentysixteen.day1 import Coord, Person
from twentysixteen.day1 import calculate_taxi_distance, calculate_taxi_distance2


@pytest.mark.parametrize('test_directions,expected', [
    (['R2', 'L3'], 5),
    (['R2', 'R2', 'R2'], 2),
    (['R5', 'L5', 'R5', 'R3'], 12)
])
def test_examples(test_directions, expected):
    assert calculate_taxi_distance(test_directions) == expected

def test_example_2():
    instructions = ['R8', 'R4', 'R4', 'R8']
    expected = 4
    result = calculate_taxi_distance2(instructions)
    assert result == expected


@pytest.mark.parametrize('current_direction,turn,new_direction', [
    ('N', 'R', 'E'),  # North, Right, East.  Etc...
    ('N', 'L', 'W'),
    ('E', 'L', 'N'),
    ('E', 'R', 'S'),
    ('S', 'R', 'W'),
    ('S', 'L', 'E'),
    ('W', 'R', 'N'),
    ('W', 'L', 'S'),
])

def test_change_direction(current_direction, turn, new_direction):
    current = Person(facing=current_direction)
    current.change_direction(turn)
    assert current.facing == new_direction

def test_coordinate_addition():
    first = Coord(x=3, y=-2)
    second = Coord(x=0, y=3)
    expected = Coord(3, 1)
    result = first + second
    assert result == expected
    assert second + first == expected

def test_coordinate_multiplication():
    first = Coord(x=3, y=-2)
    scalar = 3
    expected = Coord(9, -6)
    assert first * scalar == expected

def test_coordinate_path():
    start = Coord(3, 7)
    stop = Coord(3, 4)
    result = start.path_to(stop)

    assert isinstance(result, list)
    assert all(isinstance(c, Coord) for c in result)

    first, last = result[0], result[-1]

    assert first == start
    assert last.x == 3
    assert last.y == 5
