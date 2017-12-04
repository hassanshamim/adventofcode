import pytest

from ..day4 import DoorCode


valids = 'aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]'

def test_real_rooms():
    for datum in valids:
        door = DoorCode(datum)
        assert door.valid is True

def test_sum_sector_ids():
    expected = 1514

    doors = map(DoorCode, valids)
    total = sum(door.sector_id for door in doors)

    assert total == expected


def test_decoy_room_code():
    data = 'totally-real-room-200[decoy]'
    door = DoorCode(data)
    assert door.valid is False


def test_decryption():
    data = 'qzmt-zixmtkozy-ivhz-343[blahx]'
    expected = 'very encrypted name'

    door = DoorCode(data)

    assert door.decrypt() == expected