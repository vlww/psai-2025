import random
from collections import defaultdict

def generate_graph(num_nodes, edge_prob, min_edges):
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

    # Add random edges with given probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if j not in adjacency[i] and random.random() < edge_prob:
                adjacency[i].add(j)
                adjacency[j].add(i)

    # Output adjacency list
    for node in range(num_nodes):
        neighbors = sorted(adjacency[node])
        print(f"{node} {' '.join(map(str, neighbors))}")

# Example usage:
generate_graph(num_nodes=5, edge_prob=0.3, min_edges=1)
