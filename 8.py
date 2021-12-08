from collections import Counter


def read_day8(fname: str):
    with open(f"input/{fname}", "r") as f:
        inp = [
            [z.strip().split(" ") for z in y]
            for y in [x.strip().split("|") for x in f.readlines()]
        ]
    return inp


def find_one(lens, final, which):
    for li in lens:
        if len(li) == 5 and all([x in li for x in [final[_] for _ in which]]):
            return li


def find_69(inter, lens, digs):
    for li in lens:
        if len(li) == 6 and len(digs[inter].intersection(li)) == inter:
            return li


def one_epoch(digits, target):
    lens = [set(list(x)) for x in digits]
    digs = {}
    for i, numlen in [(1, 2), (4, 4), (7, 3), (8, 7)]:
        for li in lens:
            if len(li) == numlen:
                digs[i] = li
                break

    final = {}
    final["I"] = digs[7] - digs[1]
    # First, find the 6
    # It will be the one with one in common with 1
    # and len 6
    digs[6] = find_69(1, lens, digs)
    digs[9] = find_69(4, lens, digs)
    # Now find the zero
    for li in lens:
        if len(li) == 6 and li not in [digs[6], digs[9]]:
            digs[0] = li
            break

    final["III"] = digs[8] - digs[6]
    final["IIIIII"] = digs[1].intersection(digs[6]) - final["III"]
    final["IIIII"] = digs[8] - digs[9]
    final["IIII"] = digs[8] - digs[0]
    final["II"] = digs[4] - final["III"].union(final["IIII"]).union(final["IIIIII"])
    final["IIIIIII"] = digs[8] - set().union(*list(final.values()))

    for f in final:
        for e in final[f]:
            break
        final[f] = e

    which = {
        5: ["I", "II", "IIII", "IIIIII", "IIIIIII"],
        3: ["I", "III", "IIII", "IIIIII", "IIIIIII"],
        2: ["I", "III", "IIII", "IIIII", "IIIIIII"],
    }

    for k in which.keys():
        digs[k] = find_one(lens, final, which[k])

    finaldigs = dict([(tuple(sorted(list(v))), k) for k, v in digs.items()])
    targets = [tuple(sorted(list(x))) for x in target]
    out = []
    for t in targets:
        out.append(str(finaldigs[t]))
    return int("".join(out))


def day8(inp, task: int):
    if task == 1:
        tot = 0
        c_ = Counter([len(x) for x in inp[0][0]])
        for line in inp:
            digits, target = line
            for x in target:
                tot += int(c_[len(x)] == 1)
        return tot
    else:
        tot = 0
        for j, line in enumerate(inp):
            digits, target = line
            tot += one_epoch(digits, target)
        return tot


def main():
    test, inp = read_day8("8_test.txt"), read_day8("8.txt")
    assert day8(test, 1) == 26
    print(f"Part 1 : {day8(inp,1)}")
    assert day8(test, 2) == 61229
    print(f"Part 2 : {day8(inp,2)}")


if __name__ == "__main__":
    main()
