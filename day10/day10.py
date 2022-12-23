import re
from collections import namedtuple
import copy
import numpy as np

Command = namedtuple('Command', ['cmd', 'param'])


def parse_input():
    f = open('day10/input.txt')
    #f = open('day10/example.txt')
    lines = f.readlines()
    f.close()

    commands = []
    for line in lines:
        line = line.replace('\n', '')
        if line.startswith('addx'):
            parts = line.split()
            commands.append(Command(parts[0], int(parts[1])))
        else:
            commands.append(Command('noop', 0))

    return commands


def part_a(commands):
    cycle = 1
    x = 1
    values = []
    targets = [20 + i * 40 for i in range(6)]
    sum = 0


    for command in commands:
        if command.cmd == 'noop':
            cycle += 1
        else:
            cycle += 1
            if cycle in targets:
                values.append(x)
                sum += x * cycle
            cycle += 1
            x += command.param
        
        if cycle in targets:
            values.append(x)
            sum += x * cycle

    print(f'[a] signal strengths = {values}, sum = {sum}')


def part_b(commands):
    cycle = 0
    x = 1
    image = []
    row = []

    for command in commands:
        if len(row) >= 40:
            image.append(row)
            row = []
        if abs(cycle - x - 40 * len(image)) < 2:
            row.append('#')
        else:
            row.append('.')

        if command.cmd == 'noop':
            cycle += 1
        else:
            cycle += 1
            if len(row) >= 40:
                image.append(row)
                row = []
            if abs(cycle - x - 40 * len(image)) < 2:
                row.append('#')
            else:
                row.append('.')
            cycle += 1
            x += command.param

    image.append(row)
    print('[b] lit pixels:')
    for i in range(len(image)):
        line = ''.join(image[i])
        print(f'{line}')


def main():
    trees = parse_input()

    part_a(trees)

    part_b(trees)


if __name__ == '__main__':
    main()
