def main():
    values = create_board()
    print_board(values)

def create_board():
    values = [0, 0, 1, 0, 0, 2, 0, 0, 0]
    return values

def print_board(values):
    for i in range(9):
        if values[i] == 0:
            print(" ", end="")
        if values[i] == 1:
            print("X", end="")
        if values[i] == 2:
            print("O", end="")
        if not i%3==0:
            print("|", end="")
        if i%3==2:
            print()
            if not i==8:
                print("-------")
       


if __name__ == '__main__':
    main()