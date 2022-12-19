import re
from collections import namedtuple
import copy


Command = namedtuple('Command', ['count', 'source', 'dest'])


def parse_input():
    f = open('day05/input.txt')
    lines = f.readlines()
    f.close()

    towers = []
    commands = []
    towers_finished = False

    towers = [[] for _ in range(10)]

    for line in lines:
        if line == '\n':
            towers_finished = True
            continue

        # read towers
        if not towers_finished:
            if line[1] == '1':
                continue
            i = 0
            while i * 4 + 1 < len(line):    # 1 5 9
                crate = line[i * 4 + 1]
                if crate != ' ':
                    towers[i].append(crate)
                i += 1

        else:
            match = re.search(r'move (\d+) from (\d+) to (\d+)', line)
            commands.append(Command(int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1))
            # read commands

    return towers, commands


def part_a(towers, commands):
    for command in commands:
        for _ in range(command.count):
            towers[command.dest].insert(0, towers[command.source].pop(0))

    message = ''
    for tower in towers:
        if len(tower) > 0:
            message += tower[0]
        else:
            message += ' '
    print(f'[a] Top crates = {message}')


def part_b(towers, commands):
    for command in commands:
        for i in range(command.count):
            towers[command.dest].insert(i, towers[command.source].pop(0))

    message = ''
    for tower in towers:
        if len(tower) > 0:
            message += tower[0]
        else:
            message += ' '
    print(f'[b] Top crates = {message}')


def main():
    towers, commands = parse_input()

    part_a(copy.deepcopy(towers), commands)

    part_b(copy.deepcopy(towers), commands)


if __name__ == '__main__':
    main()
