import time

def main():
    values = create_board()
    print_board(values)
    num_turns = 0
    while True:
        values = make_move(values, num_turns)
        time.sleep(1)
        num_turns += 1
        print_board(values)
        state = check_winner(values)
        if state == 3:
            print("\nIt's a tie!")
            break
        if state == 1:
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
    player = 1 if turns % 2 == 0 else 2  # X or O
    score, best_move = minimax(values, player)

    move_name = moves[best_move]
    print(f"\nPlayer {'X' if player == 1 else 'O'} chooses: {move_name}")

    values[best_move] = player
    return values



def check_winner(values):
    # All possible winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for (i, j, k) in winning_combinations:
        if values[i] == values[j] == values[k] != 0:
            return values[i]  # 1 (X) or 2 (O)

    if all(v != 0 for v in values):
        return 3  # tie

    return 0  # game not over


def minimax(values, current_player, maximizing_player=None):
    if maximizing_player is None:
        maximizing_player = current_player

    winner = check_winner(values)
    if winner == maximizing_player:
        return (1, None)
    elif winner != 0 and winner != 3:
        return (-1, None)
    elif winner == 3:  # tie
        return (0, None)

    best_score = float('-inf') if current_player == maximizing_player else float('inf')
    best_move = None

    for i in range(9):
        if values[i] == 0:
            values[i] = current_player
            score, _ = minimax(values, 2 if current_player == 1 else 1, maximizing_player)
            values[i] = 0  # undo move

            if current_player == maximizing_player:
                if score > best_score:
                    best_score = score
                    best_move = i
            else:
                if score < best_score:
                    best_score = score
                    best_move = i

    return best_score, best_move




if __name__ == '__main__':
    main()