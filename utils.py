from typing import List
from collections import defaultdict, Counter
import numpy as np


def read_day1(fname: str):
    with open(f"input/{fname}", "r") as f:
        test = [int(x.strip()) for x in f.readlines()]
    return test


def read_day2(fname: str) -> List[List[str]]:
    with open(f"input/{fname}", "r") as f:
        insts = [x.strip().split(" ") for x in f.readlines()]
    return insts


def read_day3(fname: str) -> List[str]:
    with open(f"input/{fname}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def read_day4(fname: str):
    with open(f"input/{fname}", "r") as f:
        lines = f.readlines()
    inc = [int(x) for x in lines[0].strip().split(",")]
    i = 1
    boxes = []
    positions = defaultdict(list)
    while i < len(lines):
        if lines[i] != "\n":
            boxes.append(np.zeros((5, 5), dtype=np.int64))
            for j in range(5):
                nums = [int(x) for x in lines[i + j].strip().split(" ") if len(x) != 0]

                boxes[-1][j] = nums
                for k, num in enumerate(nums):
                    positions[num].append((len(boxes) - 1, j, k))
            i += 4
        i += 1
    return inc, boxes, positions


def read_day5(fname: str):

    with open(f"input/{fname}", "r") as f:
        lines = [
            [[int(z.strip()) for z in y.split(",")] for y in x.strip().split("->")]
            for x in f.readlines()
        ]
    return lines


def read_day6(fname: str):
    return Counter([int(x) for x in open(f"input/{fname}").read().split(",")])


def read_day7(fname: str):
    return [int(x) for x in open(f"input/{fname}", "r").read().strip().split(",")]


def read_day8(fname: str):
    with open(f"input/{fname}", "r") as f:
        inp = [
            [z.strip().split(" ") for z in y]
            for y in [x.strip().split("|") for x in f.readlines()]
        ]
    return inp
