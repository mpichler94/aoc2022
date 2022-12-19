from collections import namedtuple


Command = namedtuple('Command', ['count', 'source', 'dest'])


def parse_input():
    f = open('day06/input.txt')
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.replace('\n', '')

    return lines[0]


def part_a(datastream):
    for i in range(3, len(datastream)):
        marker = set(datastream[i-3:i+1])
        if len(marker) == 4:
            print(f'[a] Start of first packet = {i + 1}')
            return i + 1

    print('No start of packet marker found')


def part_b(datastream, sop):
    for i in range(sop + 13, len(datastream)):
        marker = set(datastream[i-13:i+1])
        if len(marker) == 14:
            print(f'[b] Start of first message = {i + 1}')
            return i + 1

    print('No start of packet marker found')


def main():
    datastream = parse_input()

    sop = part_a(datastream)

    part_b(datastream, sop - 5)


if __name__ == '__main__':
    main()
