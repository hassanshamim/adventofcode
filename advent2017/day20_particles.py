from common import puzzle_input, parse_int
from collections import defaultdict

PUZZLE_INPUT = puzzle_input(20)

def add(xs, ys): return tuple(x + y for x, y in zip(xs, ys))

class Particle:
    next_id = 0

    def __init__(self, position, velocity, acceleration):
        self.id = self.next_id
        Particle.next_id += 1

        assert len(position) == 3
        self.position = position
        assert len(velocity) == 3
        self.velocity = velocity
        assert len(acceleration) == 3
        self.acceleration = acceleration

    def __repr__(self):
        return f"Particle({self.position}, {self.velocity}, {self.acceleration})"

    @classmethod
    def from_input(cls, line):
        """Create new Particle object from puzzle input"""
        *data, _trash = line.split('>')
        data = [parse_int(triplet) for triplet in data]
        return cls(*data)

    def tick(self):
        """Simulates the passage of one frame"""
        self.velocity = add(self.velocity, self.acceleration)
        self.position = add(self.position, self.velocity)

    def distance_from_origin(self):
        return sum(map(abs, self.position))


def part1(data=PUZZLE_INPUT):

    particles = [Particle.from_input(line) for line in data]
    # brute force cuz i'm lazy.  1000 rounds might do it.
    for i in range(1000):
        for p in particles:
            p.tick()

    closest = min(particles, key=Particle.distance_from_origin)
    return closest.id


def part2(data=PUZZLE_INPUT):
    particles = {}
    for i, line in enumerate(data):
        particles[i] = Particle.from_input(line)

    for i in range(1000):
        positions = defaultdict(list)

        # do the thing, keep track of particles by position
        for pid, particle in particles.items():
            particle.tick()
            positions[particle.position].append(pid)

        # remove overlapping particles based on position
        for position, overlapping in positions.items():
            if len(overlapping) > 1:
                for particle_id in overlapping:
                    del particles[particle_id]

    return len(particles)


if __name__ == '__main__':
    print('part 1:', part1())
    print('part 2:', part2())
