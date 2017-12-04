from hashlib import md5

open_door_chars = set('bcdef')


class Path(object):
    passcode = b'yjjvjgan' # puzzle input

    def init(self):
        self.x = 0
        self.y = 0
        self.directions = []


    def neighbors(self):
        key = md5(self.passcode + self.directions).hexdigest()[:4]


def current_location(path):

    # return path.x, path.y
    y = path.count('D') - path.count('U')
    x = path.count('R') - path.count('L')
    return (x, y)


def valid_neighbors(current_path, passcode):
    key = (passcode + current_path).encode('utf8')
    key = md5(key).hexdigest()[:4]

    invalid = invalid_directions(current_path)
    order = 'UDLR'
    for direction, code in zip(order, key):
        if code in open_door_chars and direction not in invalid:
            yield direction


def invalid_directions(current_path):
    blocked = set()
    x, y = current_location(current_path)
    if x <= 0:
        blocked.add('L')
    if x >= 3:
        blocked.add('R')
    if y <= 0:
        blocked.add('U')
    if y >= 3:
        blocked.add('D')
    return blocked


def shortest_path(passcode):
    next_to_visit, discovered = [], []
    next_to_visit.append('')  # start with empty path

    while True:
        for path in next_to_visit:
            if current_location(path) == (3, 3):
                return path

            for direction in valid_neighbors(path, passcode):
                discovered.append(path + direction)
        else:
            next_to_visit, discovered = discovered, []

def longest_path(passcode):
    result = ''
    next_to_visit, discovered = [], []
    next_to_visit.append('')  # start with empty path

    while next_to_visit:
        for path in next_to_visit:
            if current_location(path) == (3, 3):
                if len(path) > len(result):
                    result = path
                    continue

            for direction in valid_neighbors(path, passcode):
                discovered.append(path + direction)
        else:
            next_to_visit, discovered = discovered, []

    return len(longest_path)



def main1():
    PUZZLE_INPUT = 'yjjvjgan'
    result = shortest_path(PUZZLE_INPUT)
    print('part 1 shortest path:', result)


if __name__ == '__main__':
    main1()
