import argparse
import numpy as np

def median(numbers):
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mean(numbers):
    return np.mean(numbers)

OPERATIONS = {
    "median": median,
    "mean": mean
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", type=float, help="Numbers you want to operate over")
    parser.add_argument("--operation", default="median", choices=["median", "mean"])
    args = parser.parse_args()
    print(OPERATIONS.get(args.operation)(args.numbers))
    
if __name__ == "__main__":
    main()