from aoc import AOCBase


class Solution(AOCBase):

    def __init__(self):
        self.day = 2
        self.input = []
        self.mp = {
            "A": 0,
            "B": 1,
            "C": 2,
            "X": 0,
            "Y": 1,
            "Z": 2
        }
        self.score = [1, 2, 3]

    def part_one(self):
        score = 0
        for i in self.input:
            opp, me = [self.mp[j] for j in i.split(" ")]
            if ((me - opp) % 3) == 1:
                score += 6
            elif me == opp:
                score += 3
            score += self.score[me]
        return score

    def part_two(self):
        score = 0
        self.mp.update({"X": -1, "Y": 0, "Z": 1})

        for i in self.input:
            opp, me = [self.mp[j] for j in i.split(" ")]
            score += (me+1) * 3
            score += self.score[((opp+me) % 3)]
        return score

    def parse_input(self, input_file):
        with open(input_file) as f:
            self.input = f.read().split("\n")
