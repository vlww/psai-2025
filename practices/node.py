class Node:
    def __init__(self, name, parent=None, cost=0):
        self.name = name
        self.parent = parent
        self.cost = cost

def main():
    A = Node("A", None, 0)
    B = Node("B", A, 1)
    C = Node("C", B, 2)
    D = Node("D", C, 3)
    path(D)

def path(node):
    nodes = []
    while node is not None:
        nodes.append(node.name)
        node = node.parent
    nodes.reverse()
    print(" → ".join(nodes))

if __name__ == "__main__":
    main()
