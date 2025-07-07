def main():
    values = create_board()
    print_board(values)
    num_turns = 0
    while True:
        values = make_move(values, num_turns)
        num_turns += 1
        print_board(values)
        state = check_winner(values)
        if state == 3:
            print("\nIt's a tie!")
            break
        if state == 1:
            print()
            print("\nX wins!")
            break
        if state == 2:
            print("\nO wins!")
            break

def create_board():
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return values

def print_board(values):
    print()
    for row in range(3):
        row_str = " "
        for col in range(3):
            i = row * 3 + col
            if values[i] == 0:
                row_str += " "
            elif values[i] == 1:
                row_str += "X"
            elif values[i] == 2:
                row_str += "O"
            if col < 2:
                row_str += "|"
        print(row_str)
        if row < 2:
            print("-------")

valid_moves = {
    "top left": 0, "top middle": 1, "top right": 2,
    "middle left": 3, "center": 4, "middle right": 5,
    "bottom left": 6, "bottom middle": 7, "bottom right": 8
}

moves = {
    0: "top left", 1: "top middle", 2: "top right",
    3: "middle left", 4: "center", 5: "middle right",
    6: "bottom left", 7: "bottom middle", 8: "bottom right"
}

def normalize_move(user_input):
    return ' '.join(user_input.lower().strip().split())

def make_move(values, turns):
    while True:
        for i in range(9):
            if(values[i]==0):
                last = i
        print("\nValid moves: ", end="")
        for i in range(9):
            if (values[i]==0):
                if(i==last):
                    print(moves[i])
                else:
                    print(moves[i], end="")
                    print(", ", end="")
        user_input = input("Choose the position where you want to move: ")
        move = normalize_move(user_input)

        if move in valid_moves:
            index = valid_moves[move]
            if values[index] != 0:
                print("That space is already taken. Try again.")
            else:
                player = 1 if turns % 2 == 0 else 2
                values[index] = player
                return values 
        else:
            print("Invalid move name, try again.")


def check_winner(values):
    full = True
    for i in values:
        if i == 0:
            full = False
    if full:
        return 3
    
    if values[0] == values[1] == values[2] != 0:
        return values[0]
    if values[3] == values[4] == values[5] != 0:
        return values[3]
    if values[6] == values[7] == values[8] != 0:
        return values[6]
    if values[0] == values[3] == values[6] != 0:
        return values[0]
    if values[1] == values[4] == values[7] != 0:
        return values[1]
    if values[2] == values[5] == values[8] != 0:
        return values[2]
    if values[0] == values[4] == values[8] != 0:
        return values[0]
    if values[2] == values[4] == values[6] != 0:
        return values[2]
    if values[0] == 1 and values[1] == 1 and values[2] == 1:
        return 1
    if values[0] == 2 and values[1] == 2 and values[2] == 2:
        return 2
    if values[3] == 1 and values[4] == 1 and values[5] == 1:
        return 1
    if values[3] == 2 and values[4] == 2 and values[5] == 2:
        return 2
    if values[6] == 1 and values[7] == 1 and values[8] == 1:
        return 1
    if values[6] == 2 and values[7] == 2 and values[8] == 2:
        return 2

    return 0



if __name__ == '__main__':
    main()