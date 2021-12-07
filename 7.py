from utils import read_day7
import numpy as np


def eulersum(n):
    return n * (n + 1) // 2


def day7(inp, task: int):
    if task == 1:
        return sum([abs(x - int(np.median(inp))) for x in inp])
    else:
        minnum, maxnum = min(inp), max(inp)

        mindist = float("inf")
        for pos in range(minnum, maxnum + 1):
            tot = 0
            for i in inp:
                tot += eulersum(abs(i - pos))
            mindist = min(tot, mindist)

        return mindist


def main():
    test, inp = read_day7("7_test.txt"), read_day7("7.txt")
    assert day7(test, 1) == 37
    print(f"Part 1 : {day7(inp,1)}")
    assert day7(test, 2) == 168
    print(f"Part 2 : {day7(inp,2)}")


if __name__ == "__main__":
    main()
