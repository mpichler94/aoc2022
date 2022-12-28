import numpy as np


def parse_input():
    f = open('input.txt')
    #f = open('example.txt')
    lines = f.readlines()
    f.close()

    # TODO: scan size
    w = 1000
    h = 500

    void_y = 0
    grid = np.zeros((h, w), dtype=int)
    for i in range(0, len(lines), 1):
        line = lines[i].strip()
        prev = None
        for pos in line.split(' -> '):
            tmp = pos.split(',')
            xy = [int(tmp[1]), int(tmp[0])]
            void_y = max(void_y, xy[0]+1)
            if prev is None:
                prev = xy
                continue

            if xy[0] == prev[0]:
                start = prev[1]
                end = xy[1]
                for y in range(min(start, end), max(start, end)+1):
                    grid[xy[0], y] = 1

            elif xy[1] == prev[1]:
                start = prev[0]
                end = xy[0]
                for x in range(min(start, end), max(start, end)+1):
                    grid[x, xy[1]] = 1

            prev = xy

    return grid, void_y


def put_sand(grid, void_y):
    s_x = 500
    s_y = 0

    while True:
        if s_y >= void_y:
            grid[s_y, s_x] = 2
            return True

        if grid[s_y+1, s_x] == 0:
            s_y += 1
        elif grid[s_y+1, s_x-1] == 0:
            s_x -= 1
            s_y += 1
        elif grid[s_y+1, s_x+1] == 0:
            s_x += 1
            s_y += 1
        else:
            break

    if s_y == 0 and s_x == 500:
        return True

    grid[s_y, s_x] = 2
    if s_y >= void_y:
        return True

    return False


def part_a(grid, void_y):

    count = 0
    while True:
        count += 1
        reached_void = put_sand(grid, void_y)
        if reached_void:
            print(f'[a] reached void after {count-1} grains of sand')
            return


def part_b(grid, void_y):

    for x in range(grid.shape[1]):
        grid[void_y+1, x] = 1

    count = 0
    while True:
        count += 1
        finished = put_sand(grid, 500)
        if finished:
            print(f'[b] filled cave after {count} grains of sand')
            return


def main():
    grid, void_y = parse_input()

    part_a(np.copy(grid), void_y)

    part_b(grid, void_y)


if __name__ == '__main__':
    main()
