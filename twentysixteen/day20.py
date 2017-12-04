import numpy as np

from common import find_data_file

PUZZLE_MAX = 4294967295




def load_data():
    def prepare(line):
        start, stop = map(int, line.split('-'))
        return slice(start, stop+1) # ranges in data source are inclusive

    with open(find_data_file()) as f:
        return [prepare(line) for line in f]


def main():
    ip_ranges = np.ones(PUZZLE_MAX+1, dtype=np.uint8)
    for blacklist in load_data():
        ip_ranges[blacklist] = 0


    print('Part 1')
    lowest_allowed_ip = np.argmax(ip_ranges)
    print('Lowest allowed IP is', lowest_allowed_ip)

    print('Part 2')
    number_allowed_ips = len(ip_ranges[ip_ranges == 1])
    print('Number of allowed ips:', number_allowed_ips)



if __name__ == '__main__':
    main()
