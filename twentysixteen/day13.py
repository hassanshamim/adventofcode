from collections import defaultdict

PUZZLE_INPUT = 1352
DESTINATION = (31, 39)
START = (1, 1)


def is_odd(x): return bool(x % 2)


def is_wall(x, y):
    result = (x*x + 3*x + 2*x*y + y + y*y)
    result += PUZZLE_INPUT
    result = bin(result).count('1')

    return is_odd(result)


def find_neighbors(coord):
    x, y = coord
    neighbors = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
    for coord in neighbors:
        if all(i >= 0 for i in coord) and not is_wall(*coord):
            yield coord


def cost_estimate(start, end, record={}):
    start_to_end = start + end
    if start_to_end not in record:
        record[start_to_end] = sum(abs(x - y) for x, y in zip(start, end))
    return record[start_to_end]


def search(start, goal):
    "A*"
    evaluated = set()
    discovered = set()
    discovered.add(start)

    came_from = dict()

    best_distance = defaultdict(lambda: float('INF'))
    best_distance[start] = 0

    estimated_cost = defaultdict(lambda: float('INF'))
    estimated_cost[start] = cost_estimate(start, goal)

    while discovered:
        current = min(discovered, key=estimated_cost.__getitem__)  # Should really be a priority queue

        discovered.remove(current)
        evaluated.add(current)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in find_neighbors(current):
            if neighbor in evaluated:
                continue

            neighbor_distance_from_current = best_distance[current] + 1

            if neighbor not in discovered:
                discovered.add(neighbor)
            elif neighbor_distance_from_current >= best_distance[neighbor]:
                continue

            # This path from current looks good
            came_from[neighbor] = current
            best_distance[neighbor] = neighbor_distance_from_current
            estimated_cost[neighbor] = best_distance[neighbor] + cost_estimate(neighbor, goal)

    return "It Broke"


def search2(start, goal):
    "A*"
    evaluated = set()
    discovered = set()
    discovered.add(start)

    came_from = dict()

    best_distance = defaultdict(lambda: float('INF'))
    best_distance[start] = 0

    estimated_cost = defaultdict(lambda: float('INF'))
    estimated_cost[start] = cost_estimate(start, goal)

    while discovered:
        current = min(discovered, key=estimated_cost.__getitem__)  # Should really be a priority queue

        discovered.remove(current)
        evaluated.add(current)

        # if current == goal:
        if best_distance[current] > 50:
            return evaluatedt
            return reconstruct_path(came_from, current)

        for neighbor in find_neighbors(current):
            if neighbor in evaluated:
                continue

            neighbor_distance_from_current = best_distance[current] + 1

            if neighbor not in discovered:
                discovered.add(neighbor)
            elif neighbor_distance_from_current >= best_distance[neighbor]:
                continue

            # This path from current looks good
            came_from[neighbor] = current
            best_distance[neighbor] = neighbor_distance_from_current
            estimated_cost[neighbor] = best_distance[neighbor] + cost_estimate(neighbor, goal)

    return "It Broke"


def nodes_in_range(start, max_distance=50):
    visited = set()

    def recurse(node, depth):
        nonlocal visited
        visited.add(node)
        for neighbor in find_neighbors(node):
            if neighbor not in visited and depth <= max_distance:
                recurse(neighbor, depth+1)

    recurse(start, 0)
    return visited


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


def main1():
    """
    Distance to destination
    """
    start = (1, 1)
    path_to_victory = search(start, DESTINATION)
    print(f"shortest path length is {len(path_to_victory)-1}")


def main2():
    """
    How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?

    122 too low
    """
    # nodes = set(nodes_from_x(START, max_distance=50))
    nodes = nodes_in_range(START, max_distance=50)
    # start = (1, 1)
    # path_to_victory = search(start, (100, 100))
    print('part2 total', len(nodes))

if __name__ == '__main__':
    # main1()
    main2()

