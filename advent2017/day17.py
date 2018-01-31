PUZZLE_INPUT = 335  # steps


def part1(steps=PUZZLE_INPUT):
    # this solution works, not sure why
    data = list()
    current_position = 0
    for i in range(1, 2018):
        N = len(data)
        next_position = ((current_position + steps) % (N + 1) + 1)
        data.insert(next_position, i)
        current_position = next_position

    return data[data.index(2017) + 1]


def part2(steps=PUZZLE_INPUT):

    zero_position = 0
    num_after_zero = None
    current_position = 0
    for i in range(1, 50000001):
        next_position = ((current_position + steps) % i + 1)
        if next_position <= zero_position:
            zero_position += 1
        elif next_position == zero_position + 1:
            num_after_zero = i

        current_position = next_position

    return num_after_zero





if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())