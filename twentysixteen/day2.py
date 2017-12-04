from functools import wraps

from common import find_data_file


def direction_maker(guard=None, adjustment=None):
    if guard is None or adjustment is None:
        raise ValueError

    def func(key):
        if key not in guard:
            return key + adjustment
        return key

    return func


KEYPAD_INSTRUCTIONS = {
    'U': direction_maker(guard=[1, 2, 3], adjustment=-3),
    'D': direction_maker(guard=[7, 8, 9], adjustment=3),
    'R': direction_maker(guard=[3, 6, 9], adjustment=1),
    'L': direction_maker(guard=[1, 4, 7], adjustment=-1),
}


def generate_bathroom_code(data, verbose=False):
    out = ''

    current = 5  # We start at 5 key

    for line in data:
        for direction in line:
            new = KEYPAD_INSTRUCTIONS[direction](current)
            if new != current:
                if verbose:
                    msg = 'Moving "{}" from {} to {}'.format(
                        direction, current, new)
                    print(msg)
                current = new
            else:
                if verbose:
                    msg = 'Cannot move "{}" from {}'.format(direction, current)
                    print(msg)
        out += str(current)
    return out


def main1():
    with open(find_data_file()) as f:
        data = f.read().splitlines()

    result = generate_bathroom_code(data)
    print('bathroom code is', result)


def ignore(*keys):
    def direction_decorator(func):
        @wraps(func)
        def func_wrapper(key):
            if key in keys:
                return key
            return func(key)

        return func_wrapper

    return direction_decorator


@ignore(1, 2, 4, 5, 9)
def up(key):
    if key in (3, 13):  # D is 13
        return key - 2
    return key - 4


@ignore(5, 9, 10, 12, 13)
def down(key):
    if key in (1, 11):
        return key + 2
    return key + 4


@ignore(1, 2, 5, 10, 13)
def left(key):
    return key - 1


@ignore(1, 4, 9, 12, 13)
def right(key):
    return key + 1


def generate_bathroom_code2(data, verbose=False):
    keycodes = '123456789ABCD'
    instructions = {'U': up, 'D': down, 'L': left, 'R': right}

    def get_keycode(position):
        # print(position)
        return keycodes[position - 1]

    out = ''

    current = 5  # We start at 5 key

    for line in data:
        for direction in line:
            new = instructions[direction](current)
            if new != current:
                if verbose:
                    msg = 'Moving "{}" from {} to {}'.format(
                        direction, get_keycode(current), get_keycode(new))
                    print(msg)
                current = new
            else:
                if verbose:
                    msg = 'Cannot move "{}" from {}'.format(
                        direction, get_keycode(current))
                    print(msg)
        out += get_keycode(current)
    return out


def main2():
    # Keypad looks like this now
    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D
    with open(find_data_file()) as f:
        data = f.read().splitlines()

    result = generate_bathroom_code2(data)
    print('bathroom code is actually', result)


if __name__ == '__main__':
    main1()
    main2()
