def part_one(inp):
    global elves
    print(max(elves.values()))


def part_two(inp):
    global elves
    val = list(elves.values())
    sum_cal = 0
    for i in range(3):
        sum_cal += max(val)
        val.remove(max(val))
    print(sum_cal)


elves = {}

with open("data/1.txt") as f:
    inp = f.read()
    each_elf = inp.split("\n\n")
    for i in range(len(each_elf)):
        elves[i] = sum(list(map(int, each_elf[i].split("\n"))))
    part_one(inp)
    part_two(inp)
