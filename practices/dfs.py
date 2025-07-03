import argparse

def dfs(start, goal, file_path):
    adjacency_list = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                split_list = line.strip().split(" ")
                parent = split_list[0]
                children = split_list[1:]
                adjacency_list[parent] = children
    except Exception as e:
        print(f"Failed to read file '{file_path}': {e}")
        return []

    stack = [start]
    visited = set([start])
    visited_list = []

    while stack:
        current = stack.pop()
        visited_list.append(current)
        if current == goal:
            break
        for neighbor in reversed(adjacency_list.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return visited_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Goal node')
    parser.add_argument('file', type=str, help='File with adjacency matrix')
    args = parser.parse_args()
    path = dfs(args.start, args.goal, args.file)
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")