from hashlib import md5
from itertools import count

puzzle_input = b'reyedfim'

def generate_password(code):
    password = ''
    for i in count(1):
        result = md5(code + str(i).encode('utf8'))
        if result.hexdigest().startswith('0' * 5):
            password += result.hexdigest()[5]
            if len(password) == 8:
                break
    return password


def generate_password2(code):
    password = ['?'] * 8
    valid_positions = list('01234567')
    for i in count(1):
        result = md5(code + str(i).encode('utf8')).hexdigest()
        if result.startswith('0' * 5) and result[5] in valid_positions:
            position, char = result[5:7]
            password[int(position)] = char
            valid_positions.remove(position)
            if not password.count('?'):
                break
    return ''.join(password)

def main1():
    result = generate_password(puzzle_input)
    print('part 1 result:', result)

def main2():
    result = generate_password2(puzzle_input)
    print('part2 result:', result)


if __name__ == '__main__':
    main2()