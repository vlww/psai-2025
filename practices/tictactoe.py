def main():
    values = create_board()
    print_board(values)
    num_turns = 0
    while True:
        values = make_move(values, num_turns)
        num_turns += 1
        print_board(values)

def create_board():
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return values

def print_board(values):
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

def normalize_move(user_input):
    return ' '.join(user_input.lower().strip().split())

def make_move(values, turns):
    while True:
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
            print("Invalid move name. Try again (e.g., 'top left').")





if __name__ == '__main__':
    main()