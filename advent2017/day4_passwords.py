from common import puzzle_input

def cat(iters): return ''.join(iters)

def part1(data=puzzle_input(4)):
    def valid(wordlist):
        return len(wordlist) == len(set(wordlist))
    return sum(map(valid, [line.split() for line in data]))

def part2(data=puzzle_input(4)):
    def valid(wordlist):
        wordlist = [cat(sorted(word)) for word in wordlist]
        return len(wordlist) == len(set(wordlist))
    return sum(map(valid, [line.split() for line in data]))
if __name__ == '__main__':
    print(part1())
    print(part2())