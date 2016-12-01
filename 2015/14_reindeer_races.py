# -*- coding: utf-8 -*-

import re

regex = re.compile(r'^(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<run_time>\d+) seconds, but then must rest for (?P<rest_time>\d+) seconds\.')

class Reindeer():
    def __init__(self, name, speed=0, run_time=0, rest_time=0):
        self.name = name
        self.speed = int(speed)
        self.run_time = int(run_time)
        self.rest_time = int(rest_time)

        self.position = 0
        self.state = None
        self.remaining_time = None

    def __repr__(self):
        return "<Reindeer {}: {} for {} more turns, at position {}".format(self.name, self.state, self.remaining_time, self.position)

    def take_turn(self):
        if not self.state:
            self.start_running()
        elif self.remaining_time == 0:
            self.switch_action()
        else:
            self.run() if self.state == 'running' else self.rest()

    def switch_action(self):
        if self.state == 'running':
            self.start_resting()
        else:
            self.start_running()

    def start_running(self):
        self.remaining_time = self.run_time
        self.state = 'running'
        self.run()

    def start_resting(self):
        self.remaining_time = self.rest_time
        self.state = 'resting'
        self.rest()

    def run(self):
        self.position += self.speed
        self.remaining_time -= 1

    def rest(self):
        self.remaining_time -= 1


def fetch_data():
    with open('./day_14.input.txt', 'r') as f:
        for line in f.readlines():
            yield line.strip()

def parse_line(line):
    return regex.match(line).groupdict()

def main():
    data = [parse_line(l) for l in fetch_data() ]
    reindeer = [Reindeer(**d) for d in data]

    race_time = 2503

    for _ in range(race_time):
        for rd in reindeer:
            rd.take_turn()

    furthest = max(rd.position for rd in reindeer)
    print('furthest is', furthest)

def main_v2():
    data = [parse_line(l) for l in fetch_data() ]
    reindeer = [Reindeer(**d) for d in data]

    race_time = 2503

    def find_furthest(reindeers):
        pos = max(rd.position for rd in reindeers)
        return [rd for rd in reindeers if rd.position == pos]

    # initialize points attribute
    for rd in reindeer:
        rd.points = 0

    for _ in range(race_time):
        for rd in reindeer: # move reindeer
            rd.take_turn()
        for rd in find_furthest(reindeer): # add points after each round
            rd.points += 1


    points = max(rd.points for rd in reindeer)
    print('winner has', points, 'points')

if __name__ == '__main__':
    main()
    main_v2()
