from utils import read_day2


def day_2(fname: str) -> int:
    insts = read_day2(fname)

    start = [0, 0]

    for dir, step in insts:
        start[0] += int(dir == "forward") * int(step)
        start[1] -= int(dir == "up") * int(step)
        start[1] += int(dir == "down") * int(step)
    return start[0] * start[1]


def day_2_p2(fname: str) -> int:
    insts = read_day2(fname)

    start = [0, 0]
    aim = 0
    for dir, step in insts:
        start[0] += int(dir == "forward") * int(step)
        start[1] += int(dir == "forward") * aim * int(step)
        aim -= int(dir == "up") * int(step)
        aim += int(dir == "down") * int(step)
    return start[0] * start[1]


def main():
    assert day_2(fname="2_test.txt") == 150
    print(f'Part 1 : {day_2("2.txt")}')
    assert day_2_p2(fname="2_test.txt") == 900
    print(f'Part 2 : {day_2_p2("2.txt")}')


if __name__ == "__main__":
    main()
