from common import load_data
from collections import Counter

def main1():
    '''find most common char in each column'''
    data = load_data()
    columns = zip(*data)

    result = []
    for col in columns:
        count = Counter()
        for char in col:
            count.update(char)
        mode = count.most_common(1)[0][0]
        result.append(mode)

    print('final answer:', ''.join(result))


def main2():
    '''
    now the least common
    '''
    data = load_data()
    columns = zip(*data)

    result = []
    for col in columns:
        count = Counter()
        for char in col:
            count.update(char)
        mode = count.most_common()[-1][0]
        result.append(mode)

    print('final answer part 2:', ''.join(result))

if __name__ == '__main__':
    main1()
    main2()
