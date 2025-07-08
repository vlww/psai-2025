class Node:
    def __init__(self, name, color, connections=None):
        self.name = name
        self.color = color
        self.connections = connections if connections is not None else []

def main():
    WA = Node("WA", None)
    NT = Node("NT", None)
    SA = Node("SA", None)
    QLD = Node("QLD", None)
    NSW = Node("NSW", None)
    V = Node("V", None)
    T = Node("T", None)

    WA.connections = [NT, SA]
    NT.connections = [WA, QLD, SA]
    SA.connections = [WA, NT, QLD, NSW, V]
    QLD.connections = [NT, SA, NSW]
    NSW.connections = [QLD, SA, V]
    V.connections = [SA, NSW]
    T.connections = []

    X = [WA, NT, SA, QLD, NSW, V, T]
    colors = ["red", "green", "blue"]
    
    print()
    brute_force(X, colors)


def factors(node1, node2):
    if node1.color == node2.color:
        return 0
    else:
        return 1

def brute_force(nodes, colors):
    steps = 0
    min_steps = None
    first_solution_found = False

    for node in nodes:
        node.color = colors[0]

    while True:
        steps += 1
        valid, conflict_edges = check(nodes)

        if valid:
            if not first_solution_found:
                min_steps = steps
                first_solution_found = True
                for node in range(len(nodes)):
                    print(f"{nodes[node].name}:{nodes[node].color} ", end="  \t" if node != len(nodes)-1 else "\n")
            break

        conflict_count = {node: 0 for node in nodes}
        for n1, n2 in conflict_edges:
            conflict_count[n1] += 1
            conflict_count[n2] += 1

        most_conflicted = max(conflict_count.items(), key=lambda x: x[1])[0]

        best_color = most_conflicted.color
        min_conflicts = len(conflict_edges)

        for color in colors:
            if color == most_conflicted.color:
                continue
            most_conflicted.color = color
            works, new_conflicts = check(nodes)
            if len(new_conflicts) < min_conflicts:
                best_color = color
                min_conflicts = len(new_conflicts)
            most_conflicted.color = best_color
        most_conflicted.color = best_color

    print("Steps taken for first solution to be found:", min_steps)    
    
def check(nodes):
    seen_edges = set()
    conflict_edges = []
    for i in nodes:
        for j in i.connections:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                if factors(i, j) == 0:
                    conflict_edges.append((i, j))
    if not conflict_edges:
        return True, []
    return False, conflict_edges


if __name__ == "__main__":
    main()
