from utils import read_day2


def day_2(fname: str, task: int) -> int:
    insts = read_day2(fname)

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
    assert day_2("2_test.txt", 1) == 150
    print(f'Part 1 : {day_2("2.txt",1)}')
    assert day_2("2_test.txt", 2) == 900
    print(f'Part 2 : {day_2("2.txt",2)}')


if __name__ == "__main__":
    main()
