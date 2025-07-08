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
        valid, wrongs = check(nodes)

        if valid:
            if not first_solution_found:
                min_steps = steps
                first_solution_found = True
                for node in range(len(nodes)):
                    print(f"{nodes[node].name}:{nodes[node].color} ", end="  \t" if node != len(nodes)-1 else "\n")
            break

        conflict_count = {node: 0 for node in nodes}
        for n1, n2 in wrongs:
            conflict_count[n1] += 1
            conflict_count[n2] += 1

        worst = max(conflict_count.items(), key=lambda x: x[1])[0]

        best_color = worst.color
        min_conflicts = len(wrongs)

        for color in colors:
            if color == worst.color:
                continue
            worst.color = color
            works, new_conflicts = check(nodes)
            if len(new_conflicts) < min_conflicts:
                best_color = color
                min_conflicts = len(new_conflicts)
            worst.color = best_color
        worst.color = best_color

    print("Steps taken for first solution to be found:", min_steps)    
    
def check(nodes):
    seen_edges = set()
    wrongs = []
    for i in nodes:
        for j in i.connections:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                if factors(i, j) == 0:
                    wrongs.append((i, j))
    if not wrongs:
        return True, []
    return False, wrongs


if __name__ == "__main__":
    main()
