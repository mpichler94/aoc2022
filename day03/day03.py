def parse_input():
    f = open('day03/input.txt')
    lines = f.readlines()
    f.close()

    rounds = []

    for line in lines:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        rounds.append(line)

    return rounds


def part_a(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        compartment1 = set(rucksack[0:len(rucksack) // 2])
        compartment2 = set(rucksack[len(rucksack) // 2:])

        both = compartment1.intersection(compartment2)
        if len(both) > 0:
            char = both.pop()
            sum += convertToNum(char)

    print(f'[a] Sum of priorities = {sum}')


def part_b(rucksacks):
    sum = 0
    for i in range(0, len(rucksacks), 3):
        rucksack1 = set(rucksacks[i])
        rucksack2 = set(rucksacks[i + 1])
        rucksack3 = set(rucksacks[i + 2])

        badge = rucksack1.intersection(rucksack2)
        badge = badge.intersection(rucksack3)

        if len(badge) > 0:
            sum += convertToNum(badge.pop())

    print(f'[b] Sum of badges = {sum}')


def convertToNum(char):
    if char.isupper():
        return ord(char) - 65 + 27
    else:
        return ord(char) - 97 + 1


def main():
    sums = parse_input()

    part_a(sums)

    part_b(sums)


if __name__ == '__main__':
    main()
