from collections import deque
import heapq
from math import prod


def is_low_point(i, j, mat):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return all(
        [
            mat[i][j] < mat[i + dir[0]][j + dir[1]]
            for dir in dirs
            if 0 <= i + dir[0] < len(mat) and 0 <= j + dir[1] < len(mat[0])
        ]
    )


def bfs(i, j, mat):
    visited = set()
    queue = deque()
    queue.append((i, j))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(queue) > 0:
        r, c = queue.popleft()

        for dir in dirs:
            if (
                0 <= r + dir[0] < len(mat)
                and 0 <= c + dir[1] < len(mat[0])
                and mat[r + dir[0]][c + dir[1]] >= mat[r][c]
                and mat[r + dir[0]][c + dir[1]] != 9
                and (r + dir[0], c + dir[1]) not in visited
            ):
                queue.append((r + dir[0], c + dir[1]))
        visited.add((r, c))
    return len(visited)


def day9(inp, task: int):
    matrix = [[int(y) for y in x] for x in inp.split("\n")]
    n, m = len(matrix), len(matrix[0])
    minheap = []
    heapq.heapify(minheap)
    heapq.heappush(minheap, 0)
    tot = 0
    for i in range(n):
        for j in range(m):
            if is_low_point(i, j, matrix):
                tot += matrix[i][j] + 1
                basinsize = bfs(i, j, matrix)
                if len(minheap) < 3:
                    heapq.heappush(minheap, basinsize)
                else:
                    elem = heapq.heappop(minheap)
                    maxelem = max(elem, basinsize)
                    heapq.heappush(minheap, maxelem)
    return tot, prod(minheap)


def main():
    test, inp = (
        open("input/9_test.txt", "r").read()[:-1],
        open("input/9.txt", "r").read()[:-1],
    )
    assert day9(test, 1)[0] == 15
    print(f"Part 1 : {day9(inp,1)[0]}")
    assert day9(test, 2)[1] == 1134
    print(f"Part 2 : {day9(inp,2)[1]}")


if __name__ == "__main__":
    main()
