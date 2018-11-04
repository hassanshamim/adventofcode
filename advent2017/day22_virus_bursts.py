"https://adventofcode.com/2017/day/22"

from common import puzzle_input

INFECTED = "#"
CLEAN = "."


def UP(row, col): return row - 1, col
def DOWN(row, col): return row + 1, col
def LEFT(row, col): return row, col - 1
def RIGHT(row, col): return row, col + 1
DIRECTIONS = [
        LEFT,
        UP,
        RIGHT,
        DOWN,
    ]  


def part1(seed=puzzle_input(22), bursts=10000):
    # count the number of times we turn a node from CLEAN to INFECTED
    INFECT_COUNT = 0

    # we use a dict to avoid extending our grid when position goes out of bounds
    grid = {
        (y, x): cell_status
        for y, row in enumerate(seed)
        for x, cell_status in enumerate(row)
    }
    map_height = max(k[0] for k in grid) + 1
    map_width = max(k[1] for k in grid) + 1
    position = (map_height // 2, map_width // 2)  # row, Col

# use for turning left/right from our direction
    current_direction = 1  # UP

    def current_node(): return grid.setdefault(position, CLEAN)

    for _ in range(bursts):
        if current_node() == INFECTED:
            current_direction = (current_direction + 1) % 4
            grid[position] = CLEAN
        else:
            current_direction = (current_direction - 1) % 4
            grid[position] = INFECTED
            INFECT_COUNT += 1
        position = DIRECTIONS[current_direction](*position)
    return INFECT_COUNT


def part2(seed=puzzle_input(22), bursts=10000000):
    INFECT_COUNT = 0

    grid = {
        (y, x): 'C' if cell_status == '.' else 'I'
        for y, row in enumerate(seed)
        for x, cell_status in enumerate(row)
    }
    map_height = max(k[0] for k in grid) + 1
    map_width = max(k[1] for k in grid) + 1
    position = (map_height // 2, map_width // 2)  # row, Col

    current_direction = 1  # UP

    def current_node(): return grid.setdefault(position, 'C')

    for _ in range(bursts):

        if current_node() == 'C':
            grid[position] = 'W'
            current_direction = (current_direction - 1) % 4
        elif current_node() == 'W':
            grid[position] = 'I'
            INFECT_COUNT += 1
        elif current_node() == 'I':
            grid[position] = 'F'
            current_direction = (current_direction + 1) % 4
        elif current_node() == 'F':
            grid[position] = 'C'
            current_direction = (current_direction + 2) % 4
        position = DIRECTIONS[current_direction](*position)
    return INFECT_COUNT



def test_part1_example():
    seed = "..#/#../...".split('/')

    result = part1(seed, bursts=7)
    assert result == 5

    result = part1(seed, bursts=70)
    assert result == 41

    result = part1(seed, bursts=10000)
    assert result == 5587


def test_part2_example():
    seed = "..#/#../...".split('/')

    assert part2(seed, bursts=100) == 26
    assert part2(seed, 10000000) == 2511944


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())