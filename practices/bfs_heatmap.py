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

def read_adjacency_list(filename):
    adjacency_list = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            node = int(parts[0])
            neighbors = list(map(int, parts[1:]))
            adjacency_list[node] = neighbors
    return adjacency_list

def generate_random_graph(num_nodes, edge_prob, min_edges):
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

def run_heatmap(node_range, prob_range, trials=5, min_edges=1):
    heatmap = []

    for num_nodes in node_range:
        row = []
        for edge_prob in prob_range:
            total_time = 0
            for _ in range(trials):
                graph = generate_random_graph(num_nodes, edge_prob, min_edges)
                start, goal = random.sample(range(num_nodes), 2)
                start_time = time.perf_counter()
                bfs(graph, start, goal)
                end_time = time.perf_counter()
                total_time += (end_time - start_time)
            avg_time_ms = (total_time / trials) * 1000
            row.append(avg_time_ms)
        heatmap.append(row)

    # Plotting
    plt.figure(figsize=(10, 7))
    data = np.array(heatmap)
    im = plt.imshow(data, cmap='viridis', origin='lower', aspect='auto')

    plt.xticks(ticks=range(len(prob_range)), labels=[f"{p:.2f}" for p in prob_range])
    plt.yticks(ticks=range(len(node_range)), labels=node_range)
    plt.xlabel("Edge Probability")
    plt.ylabel("Number of Nodes")
    plt.title("Average BFS Runtime (ms)")
    plt.colorbar(im, label='Time (ms)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, help='Start node')
    parser.add_argument('--goal', type=int, help='Goal node')
    parser.add_argument('--file', type=str, default="graph.txt", help='Graph file (adjacency list)')
    parser.add_argument('--heatmap', action='store_true', help='Generate heatmap of runtimes')
    args = parser.parse_args()

    if args.heatmap:
        node_range = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]       # y-axis
        prob_range = [0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8]    # x-axis
        run_heatmap(node_range, prob_range, trials=3)
    else:
        adj = read_adjacency_list(args.file)
        start_time = time.perf_counter()
        visited = bfs(adj, args.start, args.goal)
        end_time = time.perf_counter()
        print("Visited nodes:", visited)
        print("Runtime:", round((end_time - start_time) * 1000), "ms")
