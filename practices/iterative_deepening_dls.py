import argparse
from collections import defaultdict

def dls(start, goal, limit, adjacency_list, visited=None):
    if visited is None:
        visited = set()
    
    if limit < 0:
        return None
    
    if start == goal:
        return [start]
    
    visited.add(start)
    
    for neighbor in adjacency_list.get(start, []):
        if neighbor not in visited:
            path = dls(neighbor, goal, limit - 1, adjacency_list, visited.copy())
            if path is not None:
                return [start] + path
    return None

def ids(start, goal, adjacency_list, max_depth=50):
    for depth_limit in range(max_depth):
        path = dls(start, goal, depth_limit, adjacency_list)
        if path is not None:
            return path
    return None

def load_graph(file_path):
    adjacency_list = defaultdict(list)
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if not line.strip() or line.startswith("#"):
                    continue
                split_list = line.strip().split()
                parent = split_list[0]
                children = split_list[1:]
                adjacency_list[parent].extend(children)
    except Exception as e:
        print(f"Failed to read file '{file_path}': {e}")
        return None
    return adjacency_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Goal node')
    parser.add_argument('file', type=str, help='File with adjacency matrix')
    args = parser.parse_args()

    graph = load_graph(args.file)
    if graph is None:
        exit(1)

    path = ids(args.start, args.goal, graph)
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")
