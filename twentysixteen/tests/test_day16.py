from ..day16 import dragon_curve, flip, calculate_checksum, generate_fake_data


def test_flip():
    assert flip('101') == '010'
    assert flip('1111') == '0000'
    assert flip('0') == '1'


def test_dragon_curve_examples():
    assert dragon_curve('1') == '100'
    assert dragon_curve('0') == '001'
    assert dragon_curve('11111') == '11111000000'
    assert dragon_curve('111100001010') == '1111000010100101011110000'


def test_calculate_checksum():

    assert calculate_checksum('110010110100') == '100'


def test_generate_fake_data():
    initial = '10000'
    min_length = 20

    checksum = generate_fake_data(initial, min_length)

    assert checksum == '01100'
