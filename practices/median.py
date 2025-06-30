import argparse

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nums", nargs='+', type=float, help="List of numbers to compute the median of")
    args = parser.parse_args()

    print("Median: ", median(args.nums))
