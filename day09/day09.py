from collections import namedtuple
import numpy as np

Command = namedtuple('Command', ['direction', 'count'])


def parse_input():
    f = open('day09/input.txt')
    #f = open('day09/example.txt')
    lines = f.readlines()
    f.close()

    commands = []
    for line in lines:
        line = line.replace('\n', '')
        parts = line.split()
        commands.append(Command(parts[0], int(parts[1])))

    return commands


def move(direction, hx, hy, tx, ty):
    hx, hy = move_head(direction, hx, hy)
    tx, ty = move_tail(hx, hy, tx, ty)
    return hx, hy, tx, ty


def move_head(direction, hx, hy):
    if direction == 'U':
        hy += 1
    elif direction == 'D':
        hy -= 1
    elif direction == 'R':
        hx += 1
    elif direction == 'L':
        hx -= 1
    return hx, hy


def move_tail(hx, hy, tx, ty):
    if abs(hx - tx) > 1:
        tx += np.sign(hx - tx)
        if hy != ty:
            ty += np.sign(hy - ty)
    elif abs(hy - ty) > 1:
        ty += np.sign(hy - ty)
        if hx != tx:
            tx += np.sign(hx - tx)
    return tx, ty


def move_b(direction, pos):
    pos[0][0], pos[0][1] = move_head(direction, pos[0][0], pos[0][1])

    for i in range(1, len(pos)):
        pos[i][0], pos[i][1] = move_tail(pos[i-1][0], pos[i-1][1], pos[i][0], pos[i][1])

    return pos


def part_a(commands):
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    positions = []
    count = 0

    for command in commands:
        for _ in range(command.count):
            hx, hy, tx, ty = move(command.direction, hx, hy, tx, ty)
            pos = f'{tx}.{ty}'
            if pos not in positions:
                count += 1
                positions.append(pos)

    print(f'[a] visited fields = {count}')


def part_b(commands):
    visited = []
    count = 0
    pos = [[0, 0] for _ in range(10)]

    for command in commands:
        for _ in range(command.count):
            pos = move_b(command.direction, pos)
            position = f'{pos[9][0]}.{pos[9][1]}'
            if position not in visited:
                count += 1
                visited.append(position)

    print(f'[b] visited fields = {count}')


def main():
    trees = parse_input()

    part_a(trees)

    part_b(trees)


if __name__ == '__main__':
    main()
