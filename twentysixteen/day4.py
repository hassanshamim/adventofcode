from collections import Counter
from string import ascii_lowercase

from common import find_data_file

class DoorCode:
    def __init__(self, raw_data):
        tokens, checksum, sector_id = self.clean(raw_data)
        self.tokens = tokens
        self.checksum = checksum
        self.sector_id = sector_id


    @staticmethod
    def clean(raw):
        *tokens, last = raw.split('-')
        sector_id, checksum = last.split('[')
        sector_id = int(sector_id)
        checksum = checksum.replace(']', '')
        return tokens, checksum, sector_id

    @property
    def valid(self):
        counts = Counter(''.join(self.tokens))
        # sorting by negative count so we can sort alphabetically as well - both ascending
        sort_order = lambda item: (-item[1], item[0])
        most_common_alphabetically = sorted(counts.items(), key=sort_order)
        first_five_letters = ''.join(item[0] for item in most_common_alphabetically[:5])

        return first_five_letters == self.checksum

    def decrypt(self):
        return ' '.join(self._decrypt(word) for word in self.tokens)


    def _decrypt(self, word):
        out = ''
        for char in word:
            idx = ascii_lowercase.index(char)
            new_idx = (idx + self.sector_id) % len(ascii_lowercase)
            out += ascii_lowercase[new_idx]
        return out


def load_data():
    fpath = find_data_file()
    for line in open(fpath, 'r'):
        yield line.strip()


def main1():
    doors = map(DoorCode, load_data())
    total = sum(door.sector_id for door in doors if door.valid)
    print('Sum of Sector Ids of all valid Doors:', total)


def main2():
    """
    'What is the sector ID of the room where North Pole objects are stored?'
    Dunno what code we are looking for exactly, so just look for one with 'north' in it.
    """

    doors = map(DoorCode, load_data())
    for door in doors:
        if 'north' in door.decrypt():
            print(door.decrypt(), door.sector_id)


if __name__ == '__main__':
    main1()
    main2()