def cracker_barrel():
    positions = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1]
    print_state(positions, 6)

def print_state(list, size):
    position = 0
    for i in range(1, size+1):
        print(" "*(size-i), end="")
        for j in range(i):
            if list[position] == 0:
                print("O ", end="")
            if list[position] == 1:
                print("# ", end="")
            position += 1
        print()

def main():
    cracker_barrel()

if __name__ == "__main__":
    main()