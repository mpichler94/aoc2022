def parse_input():
    f = open('day02/input.txt')
    lines = f.readlines()
    f.close()

    rounds = []

    for line in lines:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        rounds.append(line)

    return rounds


def part_a(rounds):
    dict = {
        'AX': 4,
        'AY': 8,
        'AZ': 3,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 7,
        'CY': 2,
        'CZ': 6
    }

    score = 0
    for round in rounds:
        score += dict[round]

    print(f'[a] Score = {score}')


def part_b(rounds):
    dict = {
        'AX': 3,
        'AY': 4,
        'AZ': 8,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 2,
        'CY': 6,
        'CZ': 7
    }

    score = 0
    for round in rounds:
        score += dict[round]

    print(f'[b] Score = {score}')


def main():
    sums = parse_input()

    part_a(sums)

    part_b(sums)


if __name__ == '__main__':
    main()
