class AOCBase:

    def __init__(self):
        self.input = None
        self.day = None

    def parse_input(self, input_file):
        raise NotImplementedError

    def part_one(self):
        raise NotImplementedError

    def part_two(self):
        raise NotImplementedError

    def solve(self, input_file):
        self.parse_input(input_file)
        print("Part One: ", self.part_one())
        print("Part Two: ", self.part_two())
