from utils import read_day1
from typing import List


def day_1(inp: List[int], window: int) -> int:
    return sum([int(inp[i] > inp[i - window]) for i in range(window, len(inp))])


def main():
    test, inp = read_day1("1_test.txt"), read_day1("1.txt")
    assert day_1(test, window=1) == 7
    print(f"Part 1: {day_1(inp, window=1)}")
    assert day_1(test, 3) == 5, f"{day_1(test,3)} != 5"
    print(f"Part 2: {day_1(inp,3)}")


if __name__ == "__main__":
    main()
