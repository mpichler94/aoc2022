import itertools
import re
from collections import namedtuple
from aocd.models import Puzzle
import nographs as nog


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


def best_path(valves, rem_time):
    max_flow = 0
    for valve in valves.values():
        max_flow += valve.flow

    closed_valves = []
    for name, valve in valves.items():
        if valve.flow > 0:
            closed_valves.append(name)

    def next_edges(state, _):
        pos, closed, flow = state

        if pos in closed:
            yield (pos, closed.difference({pos}), flow + valves[pos].flow), (max_flow - flow)
        for valve in valves[pos].connections:
            yield (valve.name, closed, flow), (max_flow - flow)

    traversal = nog.TraversalShortestPaths(next_edges)
    for state in traversal.start_from(('AA', frozenset(closed_valves), 0)):
        pos, closed, flow = state
        if traversal.depth == rem_time or not closed:
            return max_flow * rem_time - traversal.distance


def best_path_2(valves, rem_time):
    max_flow = 0
    for valve in valves.values():
        max_flow += valve.flow

    closed_valves = []
    for name, valve in valves.items():
        if valve.flow > 0:
            closed_valves.append(name)

    def next_edges(state, _):
        pos, closed, flow = state

        if pos in closed:
            yield (pos, closed.difference({pos}), flow + valves[pos].flow), (max_flow - flow)
        for valve in valves[pos].connections:
            yield (valve.name, closed, flow), (max_flow - flow)

    def next_edges_b(state, _):
        pos1, pos2, closed, flow = state

        for state1, state2 in itertools.product(next_edges((pos1, closed, flow), _), next_edges((pos2, closed, flow), _)):
            (pos1, closed1, flow1), weight1 = state1
            (pos2, closed2, flow2), weight2 = state2

            if state1[0] != state2[0] or closed1 == closed:
                yield (pos1, pos2, closed1.intersection(closed2), flow1 + flow2 - flow), weight1

    traversal = nog.TraversalShortestPaths(next_edges_b)
    for state in traversal.start_from((('AA', 'AA', frozenset(closed_valves), 0))):
        pos1, pos2, closed, flow = state
        if traversal.depth == rem_time or not closed:
            return max_flow * rem_time - traversal.distance


def part_a(valves):

    return best_path(valves, 30)


def part_b(valves):

    return best_path_2(valves, 26)


def main():
    puzzle = Puzzle(2022, 16)
    ex_sensors = parse_input(puzzle.example_data)
    sensors = parse_input(puzzle.input_data)
    solution = part_a(ex_sensors)
    print(f'[a] example: {solution}')
    solution = part_a(sensors)
    print(f'[a] solution: {solution}')
    if not puzzle.answered_a:
        print('Answer [a]? (y, n): ')
        if input() == 'y':
            puzzle.answer_a = solution

    print('')

    solution = part_b(ex_sensors)
    print(f'[b] example: {solution}')
    solution = part_b(sensors)
    print(f'[b] solution: {solution}')
    if not puzzle.answered_b:
        print('Answer [b]? (y, n): ')
        if input() == 'y':
            puzzle.answer_b = solution


if __name__ == '__main__':
    main()
