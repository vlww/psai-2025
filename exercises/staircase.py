import argparse 

def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end='')
        for k in range(i+1):
            print("#", end='')
        print("")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="the size of the staircase")
    args = parser.parse_args()
    staircase(args.n)


if __name__ == "__main__":
    main()