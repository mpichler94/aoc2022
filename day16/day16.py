import re
from collections import namedtuple
from aocd.models import Puzzle

Valve = namedtuple('Valve', ['name', 'flow', 'connections'])


def parse_input(data):
    lines = data.split('\n')
    valves = {}
    for i in range(0, len(lines), 1):
        line = lines[i].strip()
        match = re.match(r'Valve (.*?) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)

        connections = match.group(3).split(', ')
        valves[match.group(1)] = Valve(match.group(1), int(match.group(2)), connections)

    for name, valve in valves.items():
        con = []
        for connection in valve.connections:
            con.append(valves[connection])
        valve.connections.clear()
        for con1 in con:
            valve.connections.append(con1)

    return valves


def best_path(pos, distances, remaining_valves, rem_time):
    pressures = []
    for valve in remaining_valves:

        distance = distances[pos.name][valve.name]

        if distance >= rem_time:
            continue

        pressure = valve.flow * (rem_time - distance - 1)

        remaining = list(remaining_valves)
        remaining.remove(valve)
        pressures.append(pressure + best_path(valve, distances, remaining, rem_time - distance - 1))

    if len(pressures) == 0:
        return 0

    return max(pressures)


def get_paths(pos, valves):
    todo = [(pos, 0)]
    lengths = {pos.name: 0}

    while len(todo) > 0:
        if len(lengths) >= len(valves):
            break
        node, length = todo.pop(0)
        if node.name not in lengths:
            lengths[node.name] = length

        for child in node.connections:
            todo.append((child, length+1))

    return lengths


def part_a(valves):

    distances = {}
    for name, valve in valves.items():
        if name == 'AA' or valve.flow > 0:
            distances[name] = get_paths(valve, valves)

    remaining_valves = []
    for valve in valves.values():
        if valve.flow > 0:
            remaining_valves.append(valve)

    return best_path(valves['AA'], distances, remaining_valves, 30)


def part_b(sensors):

    x, y = free_tile(sensors)
    print(f'[b] tuning frequency = {x * 4000000 + y}')


def main():
    puzzle = Puzzle(2022, 16)
    ex_sensors = parse_input(puzzle.example_data)
    sensors = parse_input(puzzle.input_data)
    solution = part_a(ex_sensors)
    print(f'[a] example: {solution}')
    solution = part_a(sensors)
    print(f'[a] solution: {solution}')
    print('Answer [a]? (y, n): ')
    if input() == 'y':
        puzzle.answer_a = solution

    print('')

    solution = part_b(ex_sensors)
    print(f'[b] example: {solution}')
    solution = part_b(sensors)
    print(f'[b] example: {solution}')
    print('Answer [b]? (y, n): ')
    if input() == 'y':
        puzzle.answer_b = solution


if __name__ == '__main__':
    main()
