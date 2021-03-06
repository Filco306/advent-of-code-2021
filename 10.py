import heapq
from typing import Tuple


def day10(inp: str) -> Tuple[int, int]:
    corr = {"{": "}", "(": ")", "[": "]", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    closescores = {")": 1, "]": 2, "}": 3, ">": 4}
    tot = 0
    minheap = []
    heapq.heapify(minheap)
    for line in inp.split("\n"):
        stack = []
        for char in line:

            if char in corr:
                stack.append(char)
            elif len(stack) > 0 and corr[stack[-1]] == char:
                stack.pop()
            elif len(stack) > 0 and corr[stack[-1]] != char:
                tot += points[char]
                break
        else:
            if len(stack) > 0:
                newscore = 0
                while len(stack) > 0:
                    newscore *= 5
                    newscore += closescores[corr[stack.pop()]]
                heapq.heappush(minheap, newscore)
    for _ in range(len(minheap) // 2):
        heapq.heappop(minheap)
    return tot, heapq.heappop(minheap)


def main():
    assert day10(open("input/10_test.txt", "r").read()) == (26397, 288957)
    ans1, ans2 = day10(open("input/10.txt", "r").read())
    print(f"Part 1 : {ans1}")
    print(f"Part 2 : {ans2}")


if __name__ == "__main__":
    main()
