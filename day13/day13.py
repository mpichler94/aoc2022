import copy


def parse_input():
    f = open('input.txt')
    #f = open('example.txt')
    lines = f.readlines()
    f.close()

    pairs = []
    for i in range(0, len(lines), 3):
        left_line = lines[i].strip()
        left = eval(left_line)

        right_line = lines[i+1].strip()
        right = eval(right_line)

        pairs.append([left, right])

    return pairs


def check_order(left, right, i, depth=0):
    if depth == 0:
        print('')
        print(f'== Pair {i} ==')

    print((' '*depth) + f'- Compare {left} vs {right}')

    while True:
        if type(left) == int:
            print(' ' * (depth+2) + f'- Mixed types; convert left side to {[left]} and retry comparsion')
            left = [left]
        if type(right) == int:
            print(' ' * (depth+2) + f'- Mixed types; convert right side to {[right]} and retry comparsion')
            right = [right]
        if len(left) == 0:
            if len(right) > 0:
                print(' ' * (depth+2) + '- Left side ran out of items, so inputs are in right order')
                return True, True
            else:
                return True, False
        if len(right) == 0:
            print(' ' * (depth+2) + '- Right side ran out of items, so inputs are not in right order')
            return False, True

        current_left = left.pop(0)
        current_right = right.pop(0)

        if type(current_left) == list or type(current_right) == list:
            ret, imm = check_order(current_left, current_right, i, depth+1)
            if not ret:
                return False, True
            if imm:
                return ret, True

        else:
            print(' ' * (depth+1) + f'- Compare {current_left} vs {current_right}')
            if current_left < current_right:
                print(' ' * (depth+2) + '- Left side is smaller, so inputs are in right order')
                return True, True
            if current_left > current_right:
                print(' ' * (depth+2) + '- Right side is smaller, so inputs are not in right order')
                return False, True


def part_a(pairs):
    index_sum = 0
    indices = []
    for i, pair in enumerate(pairs):
        result, _ = check_order(pair[0], pair[1], i+1)
        if result:
            index_sum += (i + 1)
            indices.append(i+1)

    print(f'[a] Sum of indices = {index_sum}')


def part_b(pairs):

    packets = [packet for packets in pairs for packet in packets]
    s_packets = [[[2]], [[6]]]

    for packet in packets:
        i = 0
        while i < len(s_packets):
            result, _ = check_order(copy.deepcopy(packet), copy.deepcopy(s_packets[i]), 0)
            if result:
                break
            i += 1
        s_packets.insert(i, packet)

        index1 = s_packets.index([[2]]) + 1
        index2 = s_packets.index([[6]]) + 1

    print('')
    print(f'[b] Decode key = {index1 * index2}')


def main():
    pairs = parse_input()

    part_a(copy.deepcopy(pairs))

    part_b(pairs)


if __name__ == '__main__':
    main()
