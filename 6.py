from collections import Counter
from utils import read_day6
from typing import List


def one_epoch(curr: Counter) -> Counter:

    new = Counter()
    for days, freq in curr.items():
        if days == 0:
            new[8] += freq
            new[6] += freq
        else:
            new[days - 1] += freq
    return new


def day6(inp: List[int], n_days: int) -> int:
    curr = inp
    for i in range(n_days):
        curr = one_epoch(curr)
    return sum(curr.values())


def main():
    test, inp = read_day6("6_test.txt"), read_day6("6.txt")
    assert day6(test, 18) == 26
    print(f"Part 1 : {day6(inp, 80)}")
    assert day6(test, 256) == 26984457539
    print(f"Part 2 : {day6(inp, 256)}")


if __name__ == "__main__":
    main()
