def parse_input():
    f = open('day01/input.txt')
    lines = f.readlines()
    f.close()

    sums = []
    calories = 0

    for line in lines:
        if line == '\n':
            sums.append(calories)
            calories = 0
            continue

        line = line.replace('\n', '')
        calories += int(line)

    return sums


def part_a(sums):
    print(f'max calories: {max(sums)}')


def part_b(sums):
    sums = sorted(sums)
    sum = sums[-1] + sums[-2] + sums[-3]
    print(f'part b: {sum}')


def main():
    sums = parse_input()

    part_a(sums)

    part_b(sums)


if __name__ == '__main__':
    main()
