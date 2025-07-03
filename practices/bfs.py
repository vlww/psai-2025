import argparse

def bfs(start, goal, file):
    adjacency_list = {}
    filename = file
    try:
        with open(filename, 'r') as file:
            for line in file:
                split_list = line.strip().split(" ")
                parent = split_list[0]
                children = split_list[1:]
                adjacency_list[parent] = children
    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return

    queue = [start]
    visited = set([start])
    parent = {start: None}  # For reconstructing the path

    while queue:
        current = queue.pop(0)
        if current == goal:
            break
        for neighbor in adjacency_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current  # Track how we got here
                queue.append(neighbor)

    # Reconstruct path from goal to start using parent dictionary
    if goal not in parent:
        return []  # No path found

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Goal node')
    parser.add_argument('file', type=str, help='File with adjacency matrix')
    args = parser.parse_args()
    print(bfs(args.start, args.goal, args.file))