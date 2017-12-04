import pytest

from day9 import decompress, decompress2

examples = [
    ('ADVENT', 'ADVENT'),
    ('A(1x5)BC', 'ABBBBBC'),
    ('(3x3)XYZ', 'XYZXYZXYZ'),
    ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
    ('(6x1)(1x3)A', '(1x3)A'),
    ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY')
]

examples2 = [
    ('(3x3)XYZ', 9),
    ('X(8x2)(3x3)ABCY', 20),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
]


@pytest.mark.parametrize('data,transformed', examples)
def test_examples(data, transformed):
    assert decompress(data) == transformed

@pytest.mark.parametrize('data,transformed', examples2)
def test_examples_part_2(data, transformed):
    assert decompress2(data) == transformed