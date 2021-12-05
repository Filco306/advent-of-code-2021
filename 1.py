from utils import read_int_list


def day_1(inp, window):
    return sum(
        int(sum(inp[(i - window) : i]) > sum(inp[(i - window - 1) : (i - 1)]))
        for i in range(window, len(inp))
    )


def main():
    test, inp = read_int_list("1_test.txt"), read_int_list("1.txt")
    assert day_1(test, window=1) == 7
    print(f"Sol part 1: {day_1(inp, window=1)}")
    assert day_1(test, 3) == 5, f"{day_1(test,3)} != 5"
    print(f"Sol part 2: {day_1(inp,3)}")


if __name__ == "__main__":
    main()
