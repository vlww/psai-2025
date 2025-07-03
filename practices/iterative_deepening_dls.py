import argparse

def dls(start, goal, limit, file):
    adjacency_list = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                split_list = line.strip().split(" ")
                parent = split_list[0]
                children = split_list[1:]
                adjacency_list[parent] = children
    except Exception as e:
        print(f"Failed to read file '{file}': {e}")
        return None

    stack = [(start, 0)]  # (node, current_depth)
    parent = {start: None}

    while stack:
        current, depth = stack.pop()
        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        if depth < limit:
            for neighbor in reversed(adjacency_list.get(current, [])):  # reverse for left-to-right order
                if neighbor not in parent:  
                    parent[neighbor] = current
                    stack.append((neighbor, depth + 1))

    return None

def ids(start, goal, file):
    depth_limit = 0
    while True:
        result = dls(start, goal, depth_limit, file)
        if result is not None:
            return result
        depth_limit += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Goal node')
    parser.add_argument('file', type=str, help='File with adjacency matrix')
    args = parser.parse_args()
    print(ids(args.start, args.goal, args.file))