import pytest

from twentysixteen.day1 import calculate_taxi_distance, Coord, Person


@pytest.mark.parametrize('test_directions,expected', [
    (['R2', 'L3'], 5),
    (['R2', 'R2', 'R2'], 2),
    (['R5', 'L5', 'R5', 'R3'], 12)
])
def test_examples(test_directions, expected):
    assert calculate_taxi_distance(test_directions) == expected


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
