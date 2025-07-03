import argparse
import random
from collections import defaultdict

def generate_graph(num_nodes, edge_prob, min_edges, output_file):
    if min_edges >= num_nodes:
        raise ValueError("min_edges must be less than the number of nodes")

    adjacency = defaultdict(set)

    # Ensure each node has at least `min_edges` connections
    for node in range(num_nodes):
        while len(adjacency[node]) < min_edges:
            target = random.randint(0, num_nodes - 1)
            if target != node and target not in adjacency[node]:
                adjacency[node].add(target)
                adjacency[target].add(node)

    # Add random edges based on edge probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if j not in adjacency[i] and random.random() < edge_prob:
                adjacency[i].add(j)
                adjacency[j].add(i)

    # Write adjacency list to file
    with open(output_file, 'w') as f:
        for node in range(num_nodes):
            neighbors = sorted(adjacency[node])
            line = f"{node} {' '.join(map(str, neighbors))}\n"
            f.write(line)

def main():
    parser = argparse.ArgumentParser(description="Generate a random undirected graph and save to a file.")
    parser.add_argument('-n', '--nodes', type=int, required=True, help="Number of nodes")
    parser.add_argument('-p', '--probability', type=float, default=0.1, help="Edge probability (0.0 - 1.0)")
    parser.add_argument('-m', '--min_edges', type=int, default=0, help="Minimum edges per node")
    parser.add_argument('-o', '--output', type=str, default="practices/generated_graph.txt", help="Output filename")

    args = parser.parse_args()

    generate_graph(args.nodes, args.probability, args.min_edges, args.output)

if __name__ == "__main__":
    main()
