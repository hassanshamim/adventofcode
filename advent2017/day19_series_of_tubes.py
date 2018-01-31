from common import puzzle_input

PUZZLE_INPUT = puzzle_input(19)

def move(current, direction):
    return current[0] + direction[0], current[1] + direction[1]

def get(postion, map):
    return map[postion[1]][postion[0]]


def main(data=PUZZLE_INPUT):
    position = (data[0].index('|'), 0) # start
    direction = (0, 1)
    letters = ''
    steps = 1

    while True:
        next_position = move(position, direction)
        next_char = get(next_position, data)

        if next_char == ' ': # game over folks
            break
        elif next_char.isalpha():
            # log it and continue
            letters += next_char

            position = next_position
            steps += 1
        elif next_char in '|-':
            # just continue as usual
            position = next_position
            steps += 1
        elif next_char == '+':
            # check either sides
            side_vectors = [(1, 0), (-1, 0)] if direction[0] == 0 else [(0, 1), (0, -1)]
            for side_direction in side_vectors:
                side_position = move(next_position, side_direction)
                side_char = get(side_position, data)

                if side_char.isalpha() or side_char in '|-':
                    # this is the direction we want to go
                    direction = side_direction
                    position = side_position
                    steps += 2
        else:
            print('uh oh')
            print(direction, '---', position)
            raise RuntimeError('oopsies')
    return letters, steps




if __name__ == '__main__':
    part1, part2 = main()
    print('part 1:', part1)
    print('part 2:', part2)