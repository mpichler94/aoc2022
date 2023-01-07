import numpy as np

from utils.aoc_base import Day


class PartA(Day):
    # Board: 0..void 1..empty 2..wall
    def parse(self, text, data):
        board = []
        lines = text.splitlines()
        end = False
        for line in lines:
            row = []
            if line == '':
                end = True
                continue
            if end:
                data.path = self.parse_path(line)
                break
            for char in line:
                if char == ' ':
                    row.append(0)
                elif char == '.':
                    row.append(1)
                elif char == '#':
                    row.append(2)
            board.append(row)

        max_len = max(len(x) for x in board) + 2
        for row in board:
            row.insert(0, 0)
            for _ in range(max_len - len(row)):
                row.append(0)
        board.insert(0, [0 for _ in range(max_len)])
        board.append([0 for _ in range(max_len)])

        data.board = np.array(board)
        data.board = np.transpose(data.board)

    @staticmethod
    def parse_path(line):
        instructions = []
        command = ''
        for char in line:
            if char.isnumeric():
                command += char
                continue

            if command != '':
                instructions.append(int(command))
                command = ''

            instructions.append(char)

        instructions.append(int(command))

        return instructions

    def compute(self, data):
        pos = self.find_start(data)
        direction = 0
        for instruction in data.path:
            if type(instruction) == str:
                if instruction == 'R':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4
                continue

            for _ in range(instruction):
                new_pos = self.step(data.board, pos, direction)
                if new_pos == pos:
                    break
                pos = new_pos

        return 1000 * pos[1] + 4 * pos[0] + direction

    @staticmethod
    def find_start(data):
        for y in range(data.board.shape[1]):
            for x in range(data.board.shape[0]):
                if data.board[x, y] == 1:
                    return x, y

        raise RuntimeError('Cannot find start position')

    @staticmethod
    def step(board, pos, direction):
        new_x = pos[0]
        new_y = pos[1]

        if direction == 0:
            new_x = pos[0] + 1
        elif direction == 2:
            new_x = pos[0] - 1
        elif direction == 1:
            new_y = pos[1] + 1
        elif direction == 3:
            new_y = pos[1] - 1
        else:
            raise RuntimeError('Invalid direction')

        if board[new_x, new_y] == 2:
            return pos

        if board[new_x, new_y] == 0:
            if direction == 0:
                for new_x in range(new_x-1, -1, -1):
                    if board[new_x, new_y] == 0 and board[new_x+1, new_y] == 1:
                        return new_x+1, new_y
            if direction == 2:
                for new_x in range(new_x+1, board.shape[0]):
                    if board[new_x, new_y] == 0 and board[new_x-1, new_y] == 1:
                        return new_x-1, new_y
            if direction == 1:
                for new_y in range(new_y-1, -1, -1):
                    if board[new_x, new_y] == 0 and board[new_x, new_y+1] == 1:
                        return new_x, new_y+1
            if direction == 3:
                for new_y in range(new_y+1, board.shape[1]):
                    if board[new_x, new_y] == 0 and board[new_x, new_y-1] == 1:
                        return new_x, new_y-1
            return pos

        return new_x, new_y

    def example_answer(self):
        return 6032


class PartB(PartA):
    pass


Day.do_day(22, 2022, PartA, PartB)
