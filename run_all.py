import os


def main():
    for name in sorted(os.listdir(os.getcwd())):
        if (
            name[-3:] == ".py"
            and len(name) in [4, 5]
            and all([x.isdigit() for x in name[:-3]])
        ):
            print(f"------ RUNNING {name} ------")
            os.system(f"python3 {name}")
            print(f"------ END OF {name} ------")
            print("\n\n")


if __name__ == "__main__":
    main()
