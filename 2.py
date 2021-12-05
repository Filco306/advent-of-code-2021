def read_p2(fname):
    with open(f"input/{fname}", "r") as f:
        insts = [x.strip().split(" ") for x in f.readlines()]
    return insts


def day_2(fname: str):
    insts = read_p2(fname)

    start = [0, 0]

    for dir, step in insts:
        start[0] += int(dir == "forward") * int(step)
        start[1] -= int(dir == "up") * int(step)
        start[1] += int(dir == "down") * int(step)
    return start[0] * start[1]


def day_2_p2(fname):
    insts = read_p2(fname)

    start = [0, 0]
    aim = 0
    for dir, step in insts:
        start[0] += int(dir == "forward") * int(step)
        start[1] += int(dir == "forward") * aim * int(step)
        aim -= int(dir == "up") * int(step)
        aim += int(dir == "down") * int(step)
    return start[0] * start[1]


assert day_2(fname="2_test.txt") == 150
print(day_2("2.txt"))
assert day_2_p2(fname="2_test.txt") == 900
print(day_2_p2("2.txt"))
