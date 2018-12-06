from common import puzzle_input

PUZZLE_INPUT = list(puzzle_input(5)[0])

def part1(data=PUZZLE_INPUT[:]):

    while True:
        for i, char in enumerate(data[:-1]):
            if char.swapcase() == data[i+1]: # we have a pair
                data.pop(i+1)
                data.pop(i)
                break # restart for loop
        else:
            return len(data)


def part2(data=PUZZLE_INPUT):
    """Like part1, but 26 times"""
    from string import ascii_lowercase

    results = []
    for letter in ascii_lowercase:
        print('calculating letter ', letter)
        letter_removed = [char for char in data if char.lower() != letter]
        results.append(part1(data=letter_removed))

    return min(results)
            

if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())