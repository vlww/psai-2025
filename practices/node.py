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

def path(Node):
    while Node.parent is not None:
        print(Node.name, "→ ", end="")
        Node = Node.parent
    print(Node.name)

if __name__ == "__main__":
    main()
