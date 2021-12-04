import numpy as np
from collections import defaultdict

def read_day4inp(fname : str):
    with open(f"input/{fname}", "r") as f:
        lines = f.readlines()
    inc = [int(x) for x in lines[0].strip().split(",")]
    i = 1
    boxes = []
    positions = defaultdict(list)
    while i < len(lines):
        if lines[i] != "\n":
            boxes.append(np.zeros((5,5), dtype=np.int64))

            for j in range(5):
                nums = [int(x) for x in lines[i+j].strip().split(" ") if len(x) != 0]

                boxes[-1][j] = nums
                for k, num in enumerate(nums):
                    positions[num].append((len(boxes)-1, j, k))
            i += 4
        i += 1
    return inc, boxes, positions

def check_vert(board, col, seen):
    for i in range(board.shape[1]):
        if board[i][col] not in seen:
            return False
    return True

def check_hori(board, row, seen):
    for i in range(board.shape[1]):
        if board[row][i] not in seen:
            return False
    return True

def get_unmarked(board, seen):
    tot = 0
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            tot += int(board[row][col] not in seen)*board[row][col]
    return tot

def day4_p1(inc, boxes, positions):
    seen = set()

    for i in inc:
        seen.add(i)
        for pos in positions[i]:
            if check_vert(boxes[pos[0]], pos[2], seen) or check_hori(boxes[pos[0]], pos[1], seen):
                return get_unmarked(boxes[pos[0]],seen)*i


def day4_p2(inc, boxes, positions):
    seen = set()
    all_boxes = set(list(range(len(boxes))))
    for i in inc:
        seen.add(i)
        for pos in positions[i]:
            if pos[0] in all_boxes and (check_vert(boxes[pos[0]], pos[2], seen) or check_hori(boxes[pos[0]], pos[1], seen)):
                all_boxes.remove(pos[0])

                if len(all_boxes) == 0:
                    return get_unmarked(boxes[pos[0]],seen)*i

def day4(fname : str, part : int):
    inc, boxes, positions = read_day4inp(fname)
    return eval(f"day4_p{part}")(inc, boxes, positions)


def main():
    assert day4("4_test.txt",1) == 4512
    print(f'Part 1 : {day4("4.txt",1)}')
    assert day4("4_test.txt",2) == 1924
    print(f'Part 2 : {day4("4.txt",2)}')


if __name__ == "__main__":
    main()
