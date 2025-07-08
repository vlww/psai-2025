from itertools import product

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

    brute_force(X, colors)


def factors(node1, node2):
    if node1.color == node2.color:
        return 0
    else:
        return 1

def brute_force(nodes, colors):
    num = [0]*len(nodes)
    def inc():
        num[0] += 1
        for i in range(len(num)-1):
            if num[i] > 2:
                num[i] = 0
                num[i+1] += 1

    while(num[-1] <= 2):
        for i in range(len(nodes)):
            nodes[i].color = colors[num[i]]
        if check(nodes):
            for node in range(len(nodes)):
                print(nodes[node].name + ":", nodes[node].color +  (", " if node != len(nodes)-1 else "\n"),  end="")
        inc()
    
    
def check(nodes):
    seen_edges = set()
    weights = []
    for i in nodes:
        for j in i.connections:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                weights.append(factors(i, j))
    product = 1
    for w in weights:
        product *= w
    if product == 1:
        return True
    return False

if __name__ == "__main__":
    main()
