# -*- coding: utf-8 -*-
"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

Your puzzle answer was 2640.

"""

import re
from itertools import islice

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


class Reindeer2:
    def __init__(self, name, speed=0, run_time=0, rest_time=0):
        speed = int(speed)
        run_time = int(run_time)
        rest_time = int(rest_time)

        def moves():
            while True:
                for i in range(run_time):
                    yield speed
                for i in range(rest_time):
                    yield 0

        self._moves = moves()
        self.name = name
        self.position = 0

    def take_turn(self):
        self.position += next(self._moves)

    def take_turns(self, n): # bonus
        self.position += sum(islice(self._moves, n))


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
    reindeer = [Reindeer2(**d) for d in data]

    race_time = 2503

    for deer in reindeer:
        deer.take_turns(race_time)

    furthest = max(rd.position for rd in reindeer)
    print('furthest is', furthest)



def main_bonus():
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
    main_bonus()
    main_v2()
