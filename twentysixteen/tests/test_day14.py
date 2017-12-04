from ..day14 import generate_hash, find_repeating_chars, valid_key, stretch_hash, chunk


def test_generate_hash():
    salt = 'abc'
    hsh = generate_hash(salt, 18)
    assert find_repeating_chars(hsh, n=3)
    assert not valid_key(hsh, index=18)


def test_known_valid():
    salt = 'abc'
    hsh = generate_hash(salt, 39)
    assert find_repeating_chars(hsh) == 'e'
    assert valid_key(salt, index=39)

    assert 'eeeee' in generate_hash(salt, 816)


def test_known_valid_2():
    salt = 'abc'
    hsh = generate_hash(salt, 92)
    assert find_repeating_chars(hsh) == '9'
    assert valid_key(salt, index=92)

    assert '99999' in generate_hash(salt, 200)

def test_stretch():
    salt = 'abc'
    hsh = generate_hash(salt, 0)

    assert hsh == '577571be4de9dcce85a041ba0410f29f'

    assert stretch_hash(hsh) == 'a107ff634856bb300138cac6568c0f24'


def test_find_repeating_chars():
    assert find_repeating_chars('2df6e9378c3c53abed6d3508b6285fff', n=3) == 'f'


def test_chunk():
    word = '1234567890'
    parts = [''.join(group) for group in chunk(word, 3)]

    assert '123' in parts
    assert '234' in parts
    assert '345' in parts
    assert '890' in parts
