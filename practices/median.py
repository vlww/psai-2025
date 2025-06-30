import argparse #lets you put argument in command line

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
    parser.add_argument("nums", nargs='+', type=float)
    args = parser.parse_args()
    print(median(args.nums))