def parse_input():
    f = open('day08/input.txt')
    #f = open('day08/example.txt')
    lines = f.readlines()
    f.close()

    trees = []
    for line in lines:
        line = line.replace('\n', '')
        row = []
        for char in line:
            row.append(int(char))
        trees.append(row)

    return trees


def part_a(trees):
    width = len(trees)
    height = len(trees[0])

    visible = 0
    for y in range(height):
        if y == 0 or y == height:
            visible += width
            continue
        for x in range(width):
            if x == 0 or x == width:
                visible += 1
                continue
            tree = trees[y][x]
            larger = 4
            for i in range(x+1, width):
                if trees[y][i] >= tree:
                    larger -= 1
                    break
            for i in range(x):
                if trees[y][i] >= tree:
                    larger -= 1
                    break
            for i in range(y+1, height):
                if trees[i][x] >= tree:
                    larger -= 1
                    break
            for i in range(y):
                if trees[i][x] >= tree:
                    larger -= 1
                    break
            if larger > 0:
                visible += 1

    print(f'[a] visible trees = {visible}')


def part_b(trees):
    width = len(trees)
    height = len(trees[0])

    scenic_score = 0
    for y in range(height):
        if y == 0 or y == height:
            continue

        for x in range(width):
            if x == 0 or x == width:
                continue

            distance = [width-x-1, x, height-y-1, y]
            tree = trees[y][x]
            for i in range(x+1, width):
                if trees[y][i] >= tree:
                    distance[0] = i-x
                    break
            for i in range(x-1, -1, -1):
                if trees[y][i] >= tree:
                    distance[1] = x - i
                    break
            for i in range(y+1, height):
                if trees[i][x] >= tree:
                    distance[2] = i-y
                    break
            for i in range(y-1, -1, -1):
                if trees[i][x] >= tree:
                    distance[3] = y - i
                    break
            score = distance[0] * distance[1] * distance[2] * distance[3]
            if score > scenic_score:
                scenic_score = score

    print(f'[b] max scenic score = {scenic_score}')


def main():
    trees = parse_input()

    part_a(trees)

    part_b(trees)


if __name__ == '__main__':
    main()
