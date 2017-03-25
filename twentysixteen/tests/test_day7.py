import pytest

from day7 import is_valid, is_invalid, supports_ssl


def test_valid_matches():
    valid_matches = [
        'abba[mnop]qrst',
        'ioxxoj[asdfgh]zxcvbn',
    ]

    for address in valid_matches:
        assert is_valid(address) == True

def test_invalid_matches():
    invalid_matches = [
        'abcd[bddb]xyyx', # repetition inside []
        'aaaa[qwer]tyui', # no repetition
        'qrcbukvnarocoao[qxokgnrdzhdtmmtrfpfb]dbjuzfg'
    ]

    for address in invalid_matches:
        assert is_invalid(address) or not is_valid(address) == True

def test_supports_ssl():
    valid_addresses = [
        'aba[bab]xyz',
        'aaa[kek]eke',
        'zazbz[bzb]cdb',
    ]

    for address in valid_addresses:
        assert supports_ssl(address) is True

def test_no_ssl_support():
    invalid_addresses = [
        'xyx[xyx]xyx'
    ]

    for address in invalid_addresses:
        assert supports_ssl(address) is False
