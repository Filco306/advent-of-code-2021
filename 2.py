from utils import read_day2


def day_2(insts, task: int) -> int:
    start = [0, 0]
    aim = 0
    for dir, step in insts:
        start[0] += int(dir == "forward") * int(step)
        start[1] += int(task == 2) * int(dir == "forward") * aim * int(step) + int(
            task == 1
        ) * (int(dir == "down") * int(step) - int(dir == "up") * int(step))
        aim += int(dir == "down") * int(step) - int(dir == "up") * int(step)
    return start[0] * start[1]


def main():
    test, inp = read_day2("2_test.txt"), read_day2("2.txt")
    assert day_2(test, 1) == 150
    print(f"Part 1 : {day_2(inp,1)}")
    assert day_2(test, 2) == 900
    print(f"Part 2 : {day_2(inp,2)}")


if __name__ == "__main__":
    main()
