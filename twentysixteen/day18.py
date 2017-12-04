PUZZLE_INPUT = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'
SAFE = '.'
TRAP = '^'



def generate_new_row(previous_row):
    # PAD previous row with safe tiles
    last = SAFE + previous_row + SAFE

    return ''.join(
        determine_tile_type(last, position)
        for position in range(1, len(last) - 1))


def determine_tile_type(previous_row, position):
    LEFT, CENTER, RIGHT = previous_row[position-1:position+2]
    if LEFT == CENTER == TRAP and RIGHT == SAFE or \
       LEFT == SAFE and CENTER == RIGHT == TRAP or \
       LEFT == TRAP and CENTER == RIGHT == SAFE or \
       RIGHT == TRAP and CENTER == LEFT == SAFE:
        return TRAP
    return SAFE


def main(n):
    """
    Starting with the map in your puzzle input, in a total of 40 rows
    (including the starting row), how many safe tiles are there?

    PART 2: How many safe tiles are there in a total of 400000 rows?
    """
    rows = [PUZZLE_INPUT]

    for _ in range(n-1):
        new_row = generate_new_row(rows[-1])
        rows.append(new_row)

    total = sum(
        sum(tile == SAFE for tile in row)
        for row in rows
    )

    print(f"RESULT for {n} rows:  {total}")


if __name__ == '__main__':
    main(40)
    main(400000)
