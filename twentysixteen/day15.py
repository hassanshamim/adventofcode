PUZZLE_INPUT = """Disc #1 has 17 positions; at time=0, it is at position 1.
Disc #2 has 7 positions; at time=0, it is at position 0.
Disc #3 has 19 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 0.
Disc #5 has 3 positions; at time=0, it is at position 0.
Disc #6 has 13 positions; at time=0, it is at position 5."""

disc_info = [(17, 1), (7, 0), (19, 2),  (5, 0), (3, 0), (13, 5)]


def make_disc_position_calculator(disc_number, num_positions, start_position):
    def calc_position(start_time):
        return (start_position + disc_number + start_time) % num_positions
    return calc_position


def earliest_win(discs):
    start_time = 0
    while True:
        if all(disc_position(start_time) == 0 for disc_position in discs):
            break
        else:
            start_time += 1


def main1():
    discs = []
    for number, details in enumerate(disc_info):
        num_positions, start_position = details
        discs.append(make_disc_position_calculator(number+1, num_positions, start_position))

    result = earliest_win(discs)
    print(result)


def main2():
    print('part 2:')

    disc_info.append((11, 0))
    discs = []
    for number, details in enumerate(disc_info):
        num_positions, start_position = details
        discs.append(make_disc_position_calculator(number+1, num_positions, start_position))

    result = earliest_win(discs)
    print(result)


if __name__ == '__main__':
    main2()
