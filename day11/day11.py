import re
import copy
import math


class Monkey:
    def __init__(self, items, operation, divisor, true_num, false_num, relief=True):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true_num = true_num
        self.false_num = false_num
        self.count = 0
        self.relief = relief

    def add_item(self, item):
        self.items.append(item)

    def round(self, monkeys, relief=True):
        self.fac = math.prod(monkey.divisor for monkey in monkeys)
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.process_item(monkeys, item, relief)

    def process_item(self, monkeys, item, relief):
        self.count += 1
        old = item
        exec(self.operation)
        item = locals()['new']
        if relief:
            item = item // 3
        else:
            item = item % self.fac
        if item % self.divisor == 0:
            monkeys[self.true_num].add_item(item)
        else:
            monkeys[self.false_num].add_item(item)


def parse_input():
    f = open('day11/input.txt')
    #f = open('day11/example.txt')
    lines = f.readlines()
    f.close()

    monkeys = []
    for i in range(0, len(lines), 7):
        items = [int(item) for item in lines[i+1][18:].split(', ')]
        op = lines[i+2].replace('Operation: ', '').strip()
        match = re.match(r'.*?(\d+)', lines[i+3])
        divisor = int(match.group(1))
        match = re.match(r'.*(\d+)', lines[i+4])
        true_num = int(match.group(1))
        match = re.match(r'.*(\d+)', lines[i+5])
        false_num = int(match.group(1))
        monkeys.append(Monkey(items, op, divisor, true_num, false_num))

    return monkeys


def round(monkeys, round, relief=True):
    for monkey in monkeys:
        monkey.round(monkeys, relief)

    if round in [0, 19, 999, 1999, 2999, 4999, 5999, 6999, 7999, 8999, 9999]:
        print(f'== After round {round+1} ==')
        for i in range(len(monkeys)):
            print(f'Monkey {i} inspects items {monkeys[i].count} times.')
        print('')

    #print('---------------------------------------------')
    #print(f'After round {round+1}:')
    #for i in range(len(monkeys)):
        #print(f'Monkey {i}: {monkeys[i].items}')


def part_a(monkeys):

    print('Part A')
    print('==============================================')
    for r in range(20):
        round(monkeys, r)

    counts = []
    print('')
    for i in range(len(monkeys)):
        print(f'Monkey {i} inspected items {monkeys[i].count} times.')
        counts.append(monkeys[i].count)

    counts.sort()
    print(f'[a] Level of monkey business = {counts[-1] * counts[-2]}')


def part_b(monkeys):

    print('Part B')
    print('==============================================')
    for r in range(10000):
        round(monkeys, r, False)

    counts = []
    print('')
    for i in range(len(monkeys)):
        print(f'Monkey {i} inspected items {monkeys[i].count} times.')
        counts.append(monkeys[i].count)

    counts.sort()
    print(f'[b] Level of monkey business = {counts[-1] * counts[-2]}')


def main():
    monkeys = parse_input()

    part_a(copy.deepcopy(monkeys))

    part_b(monkeys)


if __name__ == '__main__':
    main()
