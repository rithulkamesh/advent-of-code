from aoc import AOCBase


class Solution(AOCBase):

    def __init__(self):
        self.day = 1
        self.input = {}

    def part_one(self, inp):
        return (max(self.input.values()))

    def part_two(self, inp):
        val = list(self.input.values())
        sum_cal = 0
        for i in range(3):
            sum_cal += max(val)
            val.remove(max(val))
        return (sum_cal)

    def parse_input(self, input_file):
        with open(input_file) as f:
            inp = f.read()
            each_elf = inp.split("\n\n")
            for i in range(len(each_elf)):
                self.input[i] = sum(list(map(int, each_elf[i].split("\n"))))
