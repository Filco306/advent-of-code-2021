from utils import read_day4


def check(board, idx, seen, isrow: bool):
    for i in range(board.shape[0]):
        pos = (idx, i) if isrow else (i, idx)
        if board[pos] not in seen:
            return False
    return True


def get_unmarked(board, seen):
    tot = 0
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            tot += int(board[row][col] not in seen) * board[row][col]
    return tot


def day4_p1(i, pos, boxes, seen, cond1, cond2, all_boxes=None):
    if cond1 or cond2:
        return get_unmarked(boxes[pos[0]], seen) * i
    return None


def day4_p2(i, pos, boxes, seen, cond1, cond2, all_boxes):
    if pos[0] in all_boxes and (cond1 or cond2):
        all_boxes.remove(pos[0])

        if len(all_boxes) == 0:
            return get_unmarked(boxes[pos[0]], seen) * i
    return None


def day4(inp, part: int) -> int:
    inc, boxes, positions = inp
    seen = set()
    all_boxes = set(list(range(len(boxes)))) if part == 2 else None
    for i in inc:
        seen.add(i)
        for pos in positions[i]:
            cond1 = check(boxes[pos[0]], pos[2], seen, False)
            cond2 = check(boxes[pos[0]], pos[1], seen, True)
            res = eval(f"day4_p{part}")(i, pos, boxes, seen, cond1, cond2, all_boxes)
            if res is not None:
                return res


def main():
    test, inp = read_day4("4_test.txt"), read_day4("4.txt")
    assert day4(test, 1) == 4512
    print(f"Part 1 : {day4(inp,1)}")
    assert day4(test, 2) == 1924
    print(f"Part 2 : {day4(inp,2)}")


if __name__ == "__main__":
    main()
