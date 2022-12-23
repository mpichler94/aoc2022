import re
import copy
import math
import numpy as np
from functools import lru_cache
import sys
from collections import namedtuple


def parse_input():
    f = open('input.txt')
    #f = open('day12/example.txt')
    lines = f.readlines()
    f.close()

    grid = np.zeros((len(lines[0]), len(lines)), dtype=int)
    y = 0
    for line in lines:
        x = 0
        line = line.strip()
        for char in line:
            if char == 'S':
                grid[x, y] = 0
                start = [x, y]
            elif char == 'E':
                grid[x, y] = 25
                end = [x, y]
            else:
                grid[x, y] = (ord(char) - ord('a'))
            x += 1
        y += 1

    return grid, start, end


def process(grid, costs, starts):
    work_object = namedtuple('WorkObject', ['x', 'y', 'distance'])
    todo = set()
    for x, y in starts:
        todo.add(work_object(x, y, 0))
    visited = set()

    while len(todo) > 0:
        entry = todo.pop()
        x = entry.x
        y = entry.y

        visited.add(tuple([x, y]))
        distance = entry.distance + 1
        height = grid[x, y]
        if x > 0 and (grid[x-1, y] - height) < 2:
            if distance <= costs[x-1, y]:
                costs[x-1, y] = min(costs[x-1, y], distance)
                todo.add(work_object(x-1, y, costs[x-1, y]))

        if x < grid.shape[0]-1 and grid[x+1, y] - height < 2:
            if distance <= costs[x+1, y]:
                costs[x+1, y] = min(costs[x+1, y], distance)
                todo.add(work_object(x+1, y, costs[x+1, y]))

        if y > 0 and (grid[x, y-1] - height) < 2:
            if distance <= costs[x, y-1]:
                costs[x, y-1] = min(costs[x, y-1], distance)
                todo.add(work_object(x, y-1, costs[x, y-1]))

        if y < grid.shape[1]-1 and (grid[x, y+1] - height) < 2:
            if distance <= costs[x, y+1]:
                costs[x, y+1] = min(costs[x, y+1], distance)
                todo.add(work_object(x, y+1, costs[x, y+1]))


def part_a(grid, start, end):
    costs = np.full(grid.shape, 2000000000, dtype=int)
    costs[start[0], start[1]] = 0

    process(grid, costs, [[start[0], start[1]]])

    length = costs[end[0], end[1]]

    print(f'[a] Shortest path is {length} steps')


def part_b(grid, end):

    length = 2000000000
    starts = []
    s = np.where(grid == 0)
    for i in range(len(s[0])):
        start = [s[0][i], s[1][i]]
        costs = np.full(grid.shape, 2000000000, dtype=int)
        starts.append(start)
        costs[start[0], start[1]] = 0

    process(grid, costs, starts)

    length = min(length, costs[end[0], end[1]])

    print(f'[b] Shortest path is {length} steps')


def main():
    grid, start, end = parse_input()

    part_a(np.copy(grid), start, end)

    part_b(np.copy(grid), end)


if __name__ == '__main__':
    main()
