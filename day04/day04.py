import re


def parse_input():
    f = open('day04/input.txt')
    lines = f.readlines()
    f.close()

    rounds = []

    for line in lines:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        rounds.append(line)

    return rounds


def part_a(pairs):
    sum = 0
    for pair in pairs:
        match = re.search("^(\d+)-(\d+),(\d+)-(\d+)", pair)

        startS1 = int(match.group(1))
        startS2 = int(match.group(3))
        endS1 = int(match.group(2))
        endS2 = int(match.group(4))

        if startS1 >= startS2 and endS1 <= endS2:
            sum += 1
        elif startS2 >= startS1 and endS2 <= endS1:
            sum += 1

    print(f'[a] Sum = {sum}')


def part_b(pairs):
    sum = 0
    for pair in pairs:
        match = re.search(r"^(\d+)-(\d+),(\d+)-(\d+)", pair)

        startS1 = int(match.group(1))
        startS2 = int(match.group(3))
        endS1 = int(match.group(2))
        endS2 = int(match.group(4))
        section1 = set(range(startS1, endS1 + 1))
        section2 = set(range(startS2, endS2 + 1))

        overlap = section1.intersection(section2)
        if len(overlap) > 0:
            sum += 1

    print(f'[b] Sum = {sum}')


def main():
    sums = parse_input()

    part_a(sums)

    part_b(sums)


if __name__ == '__main__':
    main()
