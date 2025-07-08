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

    weights = []
    seen_edges = set()

    for i in X:
        for j in i.connections:
            edge = tuple(sorted([i.name, j.name]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                weights.append(factors(i, j))

    print("Weights:", weights)


def factors(node1, node2):
    if node1.color == node2.color:
        return 0
    else:
        return 1

if __name__ == "__main__":
    main()
