import argparse

def cracker_barrel(list, size):
    print_state(list, size)

def print_state(list, size):
    position = 0
    for i in range(1, size+1):
        print(" "*(size-i), end="")
        for j in range(i):
            if list[position] == 0:
                print("O ", end="")
            if list[position] == 1:
                print("# ", end="")
            position += 1
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs="+", type=int, help='The starting configuration, in 1s and 0s, separated by spaces')
    args = parser.parse_args()
    cracker_barrel(args.nums, 5)

if __name__ == "__main__":
    main()