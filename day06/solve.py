from utils.aoc_base import Day


class PartA(Day):
    def parse(self, text, data):
        data.stream = text

    def compute(self, data):
        for i in range(3, len(data.stream)):
            marker = set(data.stream[i-3:i+1])
            if len(marker) == 4:
                return i + 1

        raise RuntimeError('No start of packet marker found')

    def example_answer(self):
        return 7


class PartB(PartA):
    def compute(self, data):
        sop = PartA.compute(self, data) - 5
        for i in range(sop + 13, len(data.stream)):
            marker = set(data.stream[i-13:i+1])
            if len(marker) == 14:
                print(f'[b] Start of first message = {i + 1}')
                return i + 1

        print('No start of packet marker found')

    def example_answer(self):
        return 19


Day.do_day(6, 2022, PartA, PartB)
