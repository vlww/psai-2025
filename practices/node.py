import random

class Node:
    def __init__(self, name, parent=None, cost=0):
        self.name = name
        self.parent = parent
        self.cost = cost

def main():
    A = Node("A", None, int(random.random()*100))
    B = Node("B", A, int(random.random()*100))
    C = Node("C", B, int(random.random()*100))
    D = Node("D", C, int(random.random()*100))
    E = Node("E", D, int(random.random() * 100))
    F = Node("F", E, int(random.random() * 100))
    G = Node("G", F, int(random.random() * 100))
    H = Node("H", G, int(random.random() * 100))
    I = Node("I", H, int(random.random() * 100))
    J = Node("J", I, int(random.random() * 100))
    K = Node("K", J, int(random.random() * 100))
    L = Node("L", K, int(random.random() * 100))
    M = Node("M", L, int(random.random() * 100))
    N = Node("N", M, int(random.random() * 100))
    O = Node("O", N, int(random.random() * 100))
    P = Node("P", O, int(random.random() * 100))
    Q = Node("Q", P, int(random.random() * 100))
    R = Node("R", Q, int(random.random() * 100))
    S = Node("S", R, int(random.random() * 100))
    T = Node("T", S, int(random.random() * 100))
    U = Node("U", T, int(random.random() * 100))
    V = Node("V", U, int(random.random() * 100))
    W = Node("W", V, int(random.random() * 100))
    X = Node("X", W, int(random.random() * 100))
    Y = Node("Y", X, int(random.random() * 100))
    Z = Node("Z", Y, int(random.random() * 100))
    path(Z)
    lowest_cost(Z)

def lowest_cost(node):
    min = 999999999
    lowest_cost = None
    while node is not None:
        if node.cost < min:
            min = node.cost
            lowest_cost = node
        node = node.parent
    print("Lowest cost node:", lowest_cost.name)
    print("Cost:", min)



def path(node):
    nodes = []
    while node is not None:
        nodes.append(node.name)
        node = node.parent
    nodes.reverse()
    print(" → ".join(nodes))

if __name__ == "__main__":
    main()
