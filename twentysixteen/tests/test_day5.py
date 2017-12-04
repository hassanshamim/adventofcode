import pytest

from ..day5 import generate_password, generate_password2

@pytest.mark.skip(reason='very expensive to run')
def test_password_generation():
    door_id = b'abc'
    expected = '18f47a30'

    result = generate_password(door_id)

    assert result ==  expected

@pytest.mark.skip(reason='very expensive to run')
def test_pw_gen_version_2():
    door_id = b'abc'
    expected = '05ace8e3'

    result = generate_password2(door_id)

    assert result == expected
