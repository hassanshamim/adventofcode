from common import parse_int, puzzle_input
from collections import Counter
import pendulum as pm


def prep_input(raw_data):
    # extract timestamps
    log = []
    for line in raw_data:
        timestamp, action = line[:18], line[19:]
        timestamp = [abs(i) for i in parse_int(timestamp)]
        timestamp = pm.datetime(*timestamp)
        log.append((timestamp, action))

    # Separate by guard on duty, and generate minutes they were asleep
    log.sort()

    guard_id = None
    nap_start = None
    guard_nap_minutes = {}
    for timestamp, action in log:
        if parse_int(action):
            guard_id = parse_int(action)[0]
        elif action.endswith("falls asleep"):
            nap_start = timestamp
        elif action.endswith("wakes up"):
            duration = timestamp - nap_start
            # drop last one, which is when they wake up
            minutes = [ts.minute for ts in duration.range("minutes")][:-1]

            guard_log = guard_nap_minutes.setdefault(guard_id, [])
            guard_log.extend(minutes)

    return guard_nap_minutes


PUZZLE_INPUT = prep_input(puzzle_input(4))


def part1(data=PUZZLE_INPUT):
    # find nappiest guard, guess which minute he is asleep
    guard, naps = max(data.items(), key=lambda tup: len(tup[1]))
    most_common_minute, count = Counter(naps).most_common(1)[0]
    return guard * most_common_minute

    # find most common minute asleep among that guards naps
    # multiple the minute and guard id together


def part2(data=PUZZLE_INPUT):
    # find which guard naps most regularly

    most_frequent_minutes = [
        (guard, *Counter(minutes).most_common(1)[0]) for guard, minutes in data.items()
    ]
    guard_id, minute, count = max(most_frequent_minutes, key=lambda tup: tup[2])
    return guard_id * minute


if __name__ == "__main__":
    print("part1", part1())
    print("part2", part2())
