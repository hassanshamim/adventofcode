from hashlib import md5

salt = 'ngcjuoqr'
CACHE = {}


def chunk(word, n=3):
    for i in range(len(word) - n + 1):
        yield word[i:i+n]


def find_repeating_chars(word, n=3):
    for group in chunk(word):
        if len(set(group)) == 1:
            return group[0]


def has_repeated_char(word, char, n=5):
    for group in chunk(word, n=n):
        if set(group) == set(char):
            return True
    return False


def generate_hash(salt, index, stretch=False):
    salt = salt + str(index)
    salt = salt.encode('utf_8')
    result = md5(salt).hexdigest()

    if stretch:
        return stretch_hash(result)
    return result


def valid_key(salt, index=0, stretch=False):
    hsh = generate_hash(salt, index, stretch=stretch)
    target = find_repeating_chars(hsh)
    if not target:
        return False

    for i in range(1, 1001):
        newhash = generate_hash(salt, index=i+index, stretch=stretch)
        if has_repeated_char(newhash, target):
            return True
    return False


def stretch_hash(key):
    global CACHE
    if key in CACHE:
        return CACHE[key]

    result = key

    for i in range(2016): # provided by part 2
        result = md5(result.encode('utf8')).hexdigest()

    CACHE[key] = result

    return result



def main1():
    pad_keys = set()
    i = 0
    while len(pad_keys) is not 64:
        if valid_key(salt, index=i):
            print(f"Added key at index {i}. It is #{len(pad_keys)+1}")
            pad_keys.add(salt + str(i))

        if not i % 1000:
            print('Reached index', i)
        i += 1

    print('64th key found at index', i)


def main2():
    print('Part 2:')
    pad_keys = set()
    i = 0
    while len(pad_keys) is not 64:
        if valid_key(salt, index=i, stretch=True):
            pad_keys.add(salt + str(i))
            print(f"Added key at index {i}. It is #{len(pad_keys)}")

        if not i % 1000:
            print('Reached index', i)
        i += 1

    print('64th key found at index', i)



if __name__ == '__main__':
    main2()
