import argparse
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, deque

def bfs(adjacency_list, start, goal):
    queue = deque([start])
    visited = set([start])

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in adjacency_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

def generate_random_graph(num_nodes, edge_prob, min_edges=1):
    graph = defaultdict(set)

    for node in range(num_nodes):
        while len(graph[node]) < min_edges:
            target = random.randint(0, num_nodes - 1)
            if target != node:
                graph[node].add(target)
                graph[target].add(node)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if j not in graph[i] and random.random() < edge_prob:
                graph[i].add(j)
                graph[j].add(i)

    return {node: list(neighbors) for node, neighbors in graph.items()}

def run_heatmap(max_nodes, max_prob, steps, trials, min_edges=1):
    node_range = [int(max_nodes * (i / (steps - 1))) for i in range(steps)]
    prob_range = [max_prob * (i / (steps - 1)) for i in range(steps)]

    heatmap = []
    total_cells = steps * steps
    completed_cells = 0

    for i, num_nodes in enumerate(node_range):
        row = []
        for j, edge_prob in enumerate(prob_range):
            total_time = 0
            for _ in range(trials):
                graph = generate_random_graph(num_nodes, edge_prob, min_edges)
                if num_nodes < 2:
                    continue  # not enough nodes to sample start/goal
                start, goal = random.sample(range(num_nodes), 2)
                start_time = time.perf_counter()
                bfs(graph, start, goal)
                end_time = time.perf_counter()
                total_time += (end_time - start_time)
            avg_time_ms = (total_time / trials) * 1000
            row.append(avg_time_ms)

            # Update and print progress
            completed_cells += 1
            progress_percent = (completed_cells / total_cells) * 100
            print(f"Progress: {completed_cells}/{total_cells} ({progress_percent:.1f}%)", end='\r')
        heatmap.append(row)

    print()  # move to next line after progress
    plt.figure(figsize=(10, 7))
    data = np.array(heatmap)
    im = plt.imshow(data, cmap='viridis', origin='lower', aspect='auto')

    plt.xticks(ticks=range(steps), labels=[f"{p:.2f}" for p in prob_range])
    plt.yticks(ticks=range(steps), labels=node_range)
    plt.xlabel("Edge Probability")
    plt.ylabel("Number of Nodes")
    plt.title(f"Average BFS Runtime (ms) over {trials} Trials")
    plt.colorbar(im, label='Time (ms)')
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Generate a BFS heatmap over random graphs.")
    parser.add_argument('-n', '--max_nodes', type=int, required=True, help="Maximum number of nodes")
    parser.add_argument('-p', '--max_prob', type=float, required=True, help="Maximum edge probability (0.0 - 1.0)")
    parser.add_argument('-s', '--steps', type=int, default=6, help="Number of intervals/steps per axis (default: 6)")
    parser.add_argument('-t', '--trials', type=int, default=3, help="Trials per (nodes, prob) pair (default: 3)")
    args = parser.parse_args()

    run_heatmap(args.max_nodes, args.max_prob, args.steps, args.trials)

if __name__ == "__main__":
    main()
