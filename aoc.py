class AOCBase:

    def __init__(self):
        self.input = None

    def parse_input(self, input_file):
        raise NotImplementedError

    def part_one(self, inp):
        pass

    def part_two(self, inp):
        pass

    def solve(self, input_file):
        self.parse_input(input_file)
        print("Part One: ", self.part_one(self.input))
        print("Part Two: ", self.part_two(self.input))
