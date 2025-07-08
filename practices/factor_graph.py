import argparse

class Node:
    def __init__(self, name, neighbors=None):
        self.name = name
        self.neighbors = neighbors if neighbors is not None else []
        self.color = None


def setup_nodes():
    WA = Node("WA")
    NT = Node("NT")
    SA = Node("SA")
    QLD = Node("QLD")
    NSW = Node("NSW")
    V = Node("V")
    T = Node("T")

    WA.neighbors = [NT, SA]
    NT.neighbors = [WA, QLD, SA]
    SA.neighbors = [WA, NT, QLD, NSW, V]
    QLD.neighbors = [NT, SA, NSW]
    NSW.neighbors = [QLD, SA, V]
    V.neighbors = [SA, NSW]
    T.neighbors = []

    return [WA, NT, SA, QLD, NSW, V, T]

# BRUTE FORCE

def factors(node1, node2):
    if node1.color == node2.color:
        return 0
    else:
        return 1

def check_bruteforce(nodes):
    seen_edges = set()
    weights = []
    for i in nodes:
        for j in i.neighbors:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                weights.append(factors(i, j))
    product = 1
    for w in weights:
        product *= w
    return product == 1

def brute_force(nodes, colors):
    num = [0]*len(nodes)
    steps = 0
    min_steps = 0
    first = False

    def inc():
        num[0] += 1
        for i in range(len(num)-1):
            if num[i] > 2:
                num[i] = 0
                num[i+1] += 1

    while num[-1] <= 2:
        for i in range(len(nodes)):
            nodes[i].color = colors[num[i]]
        steps += 1
        if check_bruteforce(nodes):
            if not first:
                min_steps = steps
            first = True
            for node in range(len(nodes)):
                print(nodes[node].name + ":", nodes[node].color +  ("  \t" if node != len(nodes)-1 else "\n"),  end="")
        inc()
    print("Steps taken for first solution to be found:", min_steps)
    print("Steps taken for all solutions to be found:", steps)


# HEURISTIC

def factors_heuristic(node1, node2):
    if node1.color == node2.color:
        return 0
    else:
        return 1

def check_heuristic(nodes):
    seen_edges = set()
    wrongs = []
    for i in nodes:
        for j in i.neighbors:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                if factors_heuristic(i, j) == 0:
                    wrongs.append((i, j))
    if not wrongs:
        return True, []
    return False, wrongs

def heuristic(nodes, colors):
    steps = 0
    min_steps = None
    first_solution_found = False

    for node in nodes:
        node.color = colors[0]

    while True:
        steps += 1
        valid, wrongs = check_heuristic(nodes)

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
            works, new_conflicts = check_heuristic(nodes)
            if len(new_conflicts) < min_conflicts:
                best_color = color
                min_conflicts = len(new_conflicts)
            worst.color = best_color
        worst.color = best_color

    print("Steps taken for first solution to be found:", min_steps)


# BACKTRACKING

steps_backtrack = 0

def is_consistent_backtrack(node, color, assignment):
    global steps_backtrack
    steps_backtrack += 1
    for neighbor in node.neighbors:
        if neighbor.name in assignment and assignment[neighbor.name] == color:
            return False
    return True

def select_unassigned_variable_backtrack(nodes, assignment):
    for node in nodes:
        if node.name not in assignment:
            return node
    return None

def order_domain_values_backtrack(colors):
    return colors

def backtrack(assignment, nodes, colors):
    if len(assignment) == len(nodes):
        return assignment

    var = select_unassigned_variable_backtrack(nodes, assignment)

    for value in order_domain_values_backtrack(colors):
        if is_consistent_backtrack(var, value, assignment):
            assignment[var.name] = value
            var.color = value
            result = backtrack(assignment, nodes, colors)
            if result:
                return result
            del assignment[var.name]
            var.color = None

    return None

def backtracking_solver():
    global steps_backtrack
    steps_backtrack = 0
    nodes = setup_nodes()
    colors = ["red", "green", "blue"]
    assignment = {}

    solution = backtrack(assignment, nodes, colors)

    if solution:
        for i in range(len(nodes)):
            print(f"{nodes[i].name}:{nodes[i].color} ", end="  \t" if i != len(nodes) - 1 else "\n")
        print("Steps taken for first solution to be found:", steps_backtrack)
    else:
        print("No valid coloring found.")


# LOOKAHEAD

steps_lookahead = 0

def is_consistent_lookahead(node, color, assignment):
    global steps_lookahead
    steps_lookahead += 1
    for neighbor in node.neighbors:
        if neighbor.name in assignment and assignment[neighbor.name] == color:
            return False
    return True

def select_unassigned_variable_lookahead(nodes, assignment):
    for node in nodes:
        if node.name not in assignment:
            return node
    return None

def order_domain_values_lookahead(var, domains):
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

def backtrack_lookahead(assignment, nodes, colors, domains):
    if len(assignment) == len(nodes):
        return assignment

    var = select_unassigned_variable_lookahead(nodes, assignment)

    for value in order_domain_values_lookahead(var, domains):
        if is_consistent_lookahead(var, value, assignment):
            assignment[var.name] = value
            var.color = value

            removed = forward_check(var, value, domains, assignment)
            if removed is not None:
                result = backtrack_lookahead(assignment, nodes, colors, domains)
                if result:
                    return result
                restore_domains(domains, removed)

            del assignment[var.name]
            var.color = None
    return None

def lookahead_solver():
    global steps_lookahead
    steps_lookahead = 0
    nodes = setup_nodes()
    colors = ["red", "green", "blue"]
    assignment = {}
    domains = {node.name: colors.copy() for node in nodes}

    solution = backtrack_lookahead(assignment, nodes, colors, domains)

    if solution:
        for i in range(len(nodes)):
            print(f"{nodes[i].name}:{nodes[i].color} ", end="  \t" if i != len(nodes) - 1 else "\n")
        print("Steps taken for first solution to be found:", steps_lookahead)
    else:
        print("No valid coloring found.")

#main

def main():
    parser = argparse.ArgumentParser(description="Run different Factor Graph coloring algorithms.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--bruteforce', action='store_true', help="Run brute force solver")
    group.add_argument('--heuristic', action='store_true', help="Run heuristic solver")
    group.add_argument('--backtracking', action='store_true', help="Run backtracking solver")
    group.add_argument('--lookahead', action='store_true', help="Run lookahead solver")

    args = parser.parse_args()

    nodes = setup_nodes()
    colors = ["red", "green", "blue"]

    if args.bruteforce:
        brute_force(nodes, colors)
    elif args.heuristic:
        heuristic(nodes, colors)
    elif args.backtracking:
        backtracking_solver()
    elif args.lookahead:
        lookahead_solver()

if __name__ == "__main__":
    main()
