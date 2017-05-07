def flip(chars):
    return ''.join('1' if char == '0' else '0' for char in chars)


def dragon_curve(a):
    b = flip(reversed(a))
    return a + '0' + b


def calculate_checksum(data):
    """
    The checksum for some given data is created by considering each
    non-overlapping pair of characters in the input data. If the two
    characters match (00 or 11), the next checksum character is a 1.
    If the characters do not match (01 or 10), the next checksum character
    is a 0. This should produce a new string which is exactly half as long
    as the original. If the length of the checksum is even, repeat the process
    until you end up with a checksum with an odd length.
    """
    iter_objects = [iter(data)] * 2
    chunks = zip(*iter_objects)
    result = []

    for chunk in chunks:
        if '0' in chunk and '1' in chunk:
            result.append('0')
        else:
            result.append('1')

    if len(result) % 2 == 0:
        return calculate_checksum(result)

    return ''.join(result)


def generate_fake_data(seed, min_length):
    data = seed

    while len(data) < min_length:
        data = dragon_curve(data)

    data = data[:min_length]
    checksum = calculate_checksum(data)
    return checksum


def main1():
    puzzle_input = '11011110011011101'
    min_length = 272
    checksum = generate_fake_data(puzzle_input, min_length)
    print(f"Part 1 checksum: {checksum}")

def main2():
    puzzle_input = '11011110011011101'
    min_length = 35651584
    checksum = generate_fake_data(puzzle_input, min_length)
    print(f"Part 2 checksum: {checksum}")


if __name__ == '__main__':
    main1()
    main2()
