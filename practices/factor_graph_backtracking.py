class Node:
    def __init__(self, name, neighbors=None):
        self.name = name
        self.neighbors = neighbors if neighbors is not None else []
        self.color = None  # To track the final color assignment


steps = 0  # Global counter for consistency checks


def is_consistent(node, color, assignment):
    global steps
    steps += 1
    for neighbor in node.neighbors:
        if neighbor.name in assignment and assignment[neighbor.name] == color:
            return False
    return True


def select_unassigned_variable(nodes, assignment):
    for node in nodes:
        if node.name not in assignment:
            return node
    return None


def order_domain_values(colors):
    return colors  # Optional: apply heuristics like least-constraining-value


def backtrack(assignment, nodes, colors):
    if len(assignment) == len(nodes):
        return assignment

    var = select_unassigned_variable(nodes, assignment)

    for value in order_domain_values(colors):
        if is_consistent(var, value, assignment):
            assignment[var.name] = value
            var.color = value  # Track final color
            result = backtrack(assignment, nodes, colors)
            if result:
                return result
            del assignment[var.name]
            var.color = None

    return None


def main():
    global steps

    # Define nodes (Australian states)
    WA = Node("WA")
    NT = Node("NT")
    SA = Node("SA")
    QLD = Node("QLD")
    NSW = Node("NSW")
    V = Node("V")
    T = Node("T")

    # Define neighbors
    WA.neighbors = [NT, SA]
    NT.neighbors = [WA, SA, QLD]
    SA.neighbors = [WA, NT, QLD, NSW, V]
    QLD.neighbors = [NT, SA, NSW]
    NSW.neighbors = [QLD, SA, V]
    V.neighbors = [SA, NSW]
    T.neighbors = []  # Tasmania is isolated

    nodes = [WA, NT, SA, QLD, NSW, V, T]
    colors = ["red", "green", "blue"]
    assignment = {}

    solution = backtrack(assignment, nodes, colors)

    if solution:
        for i in range(len(nodes)):
            print(f"{nodes[i].name}:{nodes[i].color} ", end="  \t" if i != len(nodes) - 1 else "\n")
        print("Steps taken for first solution to be found:", steps)
    else:
        print("No valid coloring found.")


if __name__ == "__main__":
    main()
