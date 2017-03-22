import pytest
from ..day2 import generate_bathroom_code, KEYPAD_INSTRUCTIONS,\
                   generate_bathroom_code2


@pytest.mark.parametrize('direction,key,expected', [
    ('U',5,2),
    ('D',3,6),
    ('R',4,5),
    ('L',3,2),
])
def test_keypad_lambdas(direction, key, expected):
    result = KEYPAD_INSTRUCTIONS[direction](key)

    assert result == expected


def test_provided_example():
    instructions = 'ULL RRDDD LURDL UUUUD'.split()
    expected = '1985'

    result = generate_bathroom_code(instructions, verbose=True)

    assert expected == result


def test_provided_example2():
    instructions = 'ULL RRDDD LURDL UUUUD'.split()
    expected = '5DB3'

    result = generate_bathroom_code2(instructions, verbose=True)

    assert expected == result