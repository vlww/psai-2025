class Node:
    def __init__(self, name, neighbors=None):
        self.name = name
        self.neighbors = neighbors if neighbors is not None else []
        self.color = None

steps = 0 

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


def order_domain_values(var, domains):
    return domains[var.name] 


def forward_check(var, value, domains, assignment):
    removed = {}
    for neighbor in var.neighbors:
        if neighbor.name in assignment:
            continue
        neighbor_domain = domains[neighbor.name]
        if value in neighbor_domain:
            neighbor_domain.remove(value)
            if neighbor.name not in removed:
                removed[neighbor.name] = []
            removed[neighbor.name].append(value)
            if len(neighbor_domain) == 0:
                return None 
    return removed


def restore_domains(domains, removed):
    for var_name, values in removed.items():
        domains[var_name].extend(values)


def backtrack(assignment, nodes, colors, domains):
    if len(assignment) == len(nodes):
        return assignment

    var = select_unassigned_variable(nodes, assignment)

    for value in order_domain_values(var, domains):
        if is_consistent(var, value, assignment):
            assignment[var.name] = value
            var.color = value

            # Forward checking (lookahead)
            removed = forward_check(var, value, domains, assignment)
            if removed is not None:
                result = backtrack(assignment, nodes, colors, domains)
                if result:
                    return result
                restore_domains(domains, removed)

            del assignment[var.name]
            var.color = None
    return None


def main():
    WA = Node("WA")
    NT = Node("NT")
    SA = Node("SA")
    QLD = Node("QLD")
    NSW = Node("NSW")
    V = Node("V")
    T = Node("T")

    WA.neighbors = [NT, SA]
    NT.neighbors = [WA, SA, QLD]
    SA.neighbors = [WA, NT, QLD, NSW, V]
    QLD.neighbors = [NT, SA, NSW]
    NSW.neighbors = [QLD, SA, V]
    V.neighbors = [SA, NSW]
    T.neighbors = [] 

    nodes = [WA, NT, SA, QLD, NSW, V, T]
    colors = ["red", "green", "blue"]
    assignment = {}
    domains = {node.name: colors.copy() for node in nodes}

    solution = backtrack(assignment, nodes, colors, domains)

    if solution:
        for i in range(len(nodes)):
            print(f"{nodes[i].name}:{nodes[i].color} ", end="  \t" if i != len(nodes) - 1 else "\n")
        print("Steps taken for first solution to be found:", steps)
    else:
        print("No valid coloring found.")


if __name__ == "__main__":
    main()
