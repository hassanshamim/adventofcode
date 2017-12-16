from common import puzzle_input
from itertools import islice


def gen_maker(seed, factor):
    val = seed
    while True:
        val = (val * factor) % 2147483647
        yield val


def bottom_bin(val):
    return bin(val)[-16:]


# def test():
#     a = gen_maker(65, 16807)
#     b = gen_maker(8921, 48271)
#     res1 = list(islice(a,5))
#     res2 = list(islice(b,5))
#     assert res1 == [
#         1092455,
#         1181022009,
#         245556042,
#         1744312007,
#         1352636452,
#     ]

#     assert res2 == [
#         430625591,
#         1233683848,
#         1431495498,
#         137874439,
#         285222916,
#     ]



def test_more():
    # assert part1(65, 8921) == 588

    a = gen_maker(65, 16807)
    b = gen_maker(8921, 48271)
    a = filter(lambda i: i % 4 == 0, a)
    b = filter(lambda i: i % b == 0, b)


    assert part2(65, 8921) == 309




def part1(seed1, seed2):
    tots = 0
    a = gen_maker(seed1, 16807)
    b = gen_maker(seed2, 48271)
    for _ in range(40000000):
        anext = next(a)
        bnext = next(b)
        x = bottom_bin(anext)
        y = bottom_bin(bnext)
        if x == y:
            tots += 1

    return tots



def part2(seed1, seed2):
    """
    original: 44.87s user 0.29s system 99% cpu 45.552 total
    lazy:     37.94s user 0.09s system 99% cpu 38.118 total
    """
    a = gen_maker(seed1, 16807)
    b = gen_maker(seed2, 48271)
    a = filter(lambda x: x % 4 == 0, a)
    b = filter(lambda x: x % 8 == 0, b)
    a = map(bottom_bin, a)
    b = map(bottom_bin, b)
    pairs = zip(a, b)
    pairs = islice(pairs, 5000000)
    return sum(x == y for x, y in pairs)

if __name__ == '__main__':
    puzzle_input = 116, 299
    # print('part 1:', part1(*puzzle_input))
    print('part 2:', part2(*puzzle_input))