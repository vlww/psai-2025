import argparse
import time

def bfs(start, goal):
    adjacency_list = {}
    filename = "ProblemSolvingWithAI/graphs/graph_1000.txt"
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
    visited_list = []

    while queue:
        #print(queue)
        current = queue.pop(0)
        visited_list.append(current)
        if current == goal:
            break
        for neighbor in adjacency_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, help='Start node')
    parser.add_argument('goal', type=str, help='Start node')
    args = parser.parse_args()
    start_time = time.perf_counter()
    print(bfs(args.start, args.goal))
    end_time = time.perf_counter()
    runtime = round((end_time-start_time)*1000)
    print("Runtime:", (runtime), "ms")
