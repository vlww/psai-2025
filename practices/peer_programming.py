import argparse

def find_all_indices_from_file(filename, target):
    try:
        with open(filename, 'r') as file:
            listt = [int(line.strip()) for line in file if line.strip() != '']
    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return

    try:
        target = int(target)
    except ValueError:
        print(f"Target must be an integer, got '{target}'")
        return

    indices = [i for i, value in enumerate(listt) if value == target]

    if indices:
        for idx in indices:
            print(idx)
    else:
        print(-1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='Target number to find in list.txt')
    args = parser.parse_args()
    find_all_indices_from_file('practices/list.txt', args.target)
