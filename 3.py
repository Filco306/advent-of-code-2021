from typing import Callable, List
from utils import read_day3


def bitcrit1(lines: List[str], i: int) -> int:
    num = sum([int(x[i]) for x in lines]) / len(lines)
    return 0 if num < 0.5 else 1


def bitcrit2(lines: List[str], i: int) -> int:
    return 1 - bitcrit1(lines, i)


def findnum(lines: List[str], bitcrit: Callable) -> int:
    i = 0
    while i < len(lines[0]) and len(lines) > 1:
        value = bitcrit(lines, i)
        lines = [x for x in lines if int(x[i]) == value]
        i += 1
    assert len(lines) == 1
    return int(lines[0], 2)


def day_3(lines, task: int):
    # lines = read_day3(fname)
    if task == 1:
        nums = []
        for i in range(len(lines[0])):
            tot = 0
            for j in range(len(lines)):
                tot += int(lines[j][i])
            nums.append(tot / len(lines))
        gamma = int("".join([str(round(x)) for x in nums]), 2)
        epsilon = int("".join([str(round(1 - x)) for x in nums]), 2)
        return gamma * epsilon
    else:
        oxy = findnum(lines, bitcrit1)
        co2 = findnum(lines, bitcrit2)
        return oxy * co2


def main():
    test, inp = read_day3("3_test.txt"), read_day3("3.txt")
    assert day_3(test, 1) == 198
    print(f"Part 1 : {day_3(inp,1)}")

    assert day_3(test, 2) == 230
    print(f"Part 2 : {day_3(inp,2)}")


if __name__ == "__main__":
    main()
