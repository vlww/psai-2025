import argparse

def find_index_from_file(filename, target):
    try:
        with open(filename, 'r') as file:
            # Read all lines and convert to integers
            listt = [int(line.strip()) for line in file if line.strip() != '']
    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return -1

    try:
        target = int(target)
    except ValueError:
        print(f"Target must be an integer, got '{target}'")
        return -1

    for i, value in enumerate(listt):
        if value == target:
            print(i)
            return i
    print(-1)
    return -1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='Target number to find in list.txt')
    args = parser.parse_args()
    find_index_from_file('practices/list.txt', args.target)
