import argparse
from collections import defaultdict, deque

def bfs(start, goal, file_path):
    adjacency_list = defaultdict(list)
    
    # Read the graph from file and build adjacency list (undirected)
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                # Split on whitespace (spaces or tabs)
                split_list = line.split()
                parent = split_list[0]
                children = split_list[1:]
                
                # Add edges (parent -> children)
                adjacency_list[parent].extend(children)
                
                # Add reverse edges for undirected graph (children -> parent)
                for child in children:
                    if parent not in adjacency_list[child]:
                        adjacency_list[child].append(parent)
                        
    except Exception as e:
        print(f"Failed to read file '{file_path}': {e}")
        return []

    # After building adjacency_list
    for node in adjacency_list:
        adjacency_list[node].sort()


    # BFS setup
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # To reconstruct path

    # BFS loop
    while queue:
        current = queue.popleft()
        # Debug current node and queue state
        
        if current == goal:
            break
        
        for neighbor in adjacency_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Reconstruct path if goal was reached
    if goal not in parent:
        print(f"No path found from '{start}' to '{goal}'.")
        return []

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="BFS pathfinder")
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Goal node')
    parser.add_argument('file', type=str, help='File with adjacency list')
    args = parser.parse_args()
    bfs_path = bfs(args.start, args.goal, args.file)

    if bfs_path:
        print(" -> ".join(bfs_path))
    else:
        print("No path found.")

