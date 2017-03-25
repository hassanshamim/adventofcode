import re
from itertools import filterfalse as reject

from common import load_data


INVALID_IP = re.compile(r'\[\w*(\w)(?!\1)(\w)\2\1\w*\]')
VALID_IP = re.compile(r'(\w)(?!\1)(\w)\2\1')
DELIMITER = re.compile(r'[\[\]]')
ABA_SEQUENCE = re.compile(r'(?=(\w)(?!\1)(\w)\1)')


def is_valid(address):
    return bool(VALID_IP.search(address))


def is_invalid(address):
    return bool(INVALID_IP.search(address))


def split_address(address):
    parts = DELIMITER.split(address)
    parts = list(filter(bool, parts)) # remove empty strings
    supernet_sequences = parts[::2]
    hypernet_sequences = parts[1::2]
    return supernet_sequences, hypernet_sequences


def extract_aba(sequences):
    for sequence in sequences:
        yield from ABA_SEQUENCE.findall(sequence)


def supports_ssl(address):
    """
    Has ABA sequence outside [] and BAB sequence inside []
    """

    supernet, hypernet = split_address(address)
    matches = extract_aba(supernet)

    for a, b in matches:
        bab = b + a + b

        if any(bab in part for part in hypernet):
            return True
    return False


def main1():
    addresses = load_data()
    invalid_removed = reject(is_invalid, addresses)
    valids = [address for address in invalid_removed if is_valid(address)]
    valid_count = len(valids)
    print('total valid ips:', valid_count)
    return valids


def main2():
    addresses = load_data()

    ssl_count = sum(map(supports_ssl, addresses))
    print(ssl_count, 'addresses support ssl')

if __name__ == '__main__':
    main1()
    main2()
