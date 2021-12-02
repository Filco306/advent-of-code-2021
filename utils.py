
def read_int_list(fname : str):
    with open(f"input/{fname}","r") as f:
        test = [int(x.strip()) for x in f.readlines()]
    return test
