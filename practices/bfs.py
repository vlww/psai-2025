def bfs(filename):
    try:
        with open(filename, 'r') as file:
            unsorted_list = [int(line.strip()) for line in file if line.strip() != '']
    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return

if __name__ == '__main__':
    print(bfs('practices/list.txt'))