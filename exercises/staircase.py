import argparse 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="Number of stairs")
    args = parser.parse_args()
    for i in range(args.num):
        for j in range(args.num-i-1):
            print(" ", end='')
        for k in range(i+1):
            print("#", end='')
        print("")


if __name__ == "__main__":
    main()