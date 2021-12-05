from collections import Counter
from utils import read_day5


def add_to_counter(start, end, idx, counter):
    startpos, endpos = (
        min(start[1 - idx], end[1 - idx]),
        max(start[1 - idx], end[1 - idx]) + 1,
    )
    for i in range(startpos, endpos):
        pos = (start[0], i) if idx == 0 else (i, start[1])
        counter[pos] += 1


def add_diag(start, end, counter):
    positions = sorted([start, end])
    startpos, endpos = positions.copy()
    while startpos[0] <= endpos[0]:
        counter[(startpos[0], startpos[1])] += 1
        startpos[0] += 1
        startpos[1] += int(startpos[1] < endpos[1]) - int(startpos[1] > endpos[1])


def day5(fname: str, task: int):
    lines = read_day5(fname)
    counter = Counter()
    for start, end in lines:
        if start[0] == end[0] or start[1] == end[1]:
            add_to_counter(start, end, int(start[1] == end[1]), counter)
        elif task == 2:
            # Otherwise it is a diagonal and we should
            # only do it if is task 2
            add_diag(start, end, counter)
    return sum([v >= 2 for v in counter.values()])


def main():
    assert day5("5_test.txt", 1) == 5
    print(f'Part 1 : {day5("5.txt", 1)}')
    assert day5("5_test.txt", 2) == 12
    print(f'Part 2 : {day5("5.txt", 2)}')


if __name__ == "__main__":
    main()
