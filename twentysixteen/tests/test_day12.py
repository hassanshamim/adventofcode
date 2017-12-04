from day12 import execute

part_1_example = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".splitlines()


def test_example():
    output = execute(part_1_example)
    assert output['a'] == 42
