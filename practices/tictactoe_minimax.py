import argparse
import time

valid_moves = {
    "top left": 0, "top middle": 1, "top right": 2,
    "middle left": 3, "center": 4, "middle right": 5,
    "bottom left": 6, "bottom middle": 7, "bottom right": 8
}
moves = {v: k for k, v in valid_moves.items()}


def normalize_move(user_input):
    return ' '.join(user_input.lower().strip().split())


def create_board():
    return [0] * 9


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


def check_winner(values):
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for (i, j, k) in combos:
        if values[i] == values[j] == values[k] != 0:
            return values[i]
    if all(v != 0 for v in values):
        return 3  # Tie
    return 0  # Game not over


def minimax(values, current_player, depth, maximizing_player=None):
    if maximizing_player is None:
        maximizing_player = current_player

    winner = check_winner(values)
    if winner == maximizing_player:
        return (1, None)
    elif winner != 0 and winner != 3:
        return (-1, None)
    elif winner == 3:
        return (0, None)

    best_score = float('-inf') if current_player == maximizing_player else float('inf')
    best_move = None

    for i in range(9):
        if values[i] == 0:
            values[i] = current_player
            score, _ = minimax(values, 2 if current_player == 1 else 1, depth-1, maximizing_player)
            values[i] = 0
            if current_player == maximizing_player:
                if score > best_score:
                    best_score = score
                    best_move = i
            else:
                if score < best_score:
                    best_score = score
                    best_move = i

    return best_score, best_move


def ai_move(values, player):
    score, move = minimax(values, player, depth=0)
    print(f"\n{'X' if player == 1 else 'O'} chooses: {moves[move]}")
    print(f"Utility: {score}")
    values[move] = player
    return values


def human_move(values, player):
    print("\nYour valid moves:")
    for i in range(9):
        if values[i] == 0:
            print(f"- {moves[i]}")
    while True:
        user_input = input("Your move: ")
        move = normalize_move(user_input)
        if move in valid_moves:
            index = valid_moves[move]
            if values[index] == 0:
                values[index] = player
                return values
            else:
                print("That space is taken. Try again.")
        else:
            print("Invalid move name. Try again.")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--ai', action='store_true', help="AI vs AI mode")
    group.add_argument('--human', action='store_true', help="Human vs AI mode (you play as X)")
    args = parser.parse_args()

    mode = "ai_vs_ai" if args.ai else "human_vs_ai"
    values = create_board()
    print_board(values)
    num_turns = 0

    while True:
        current_player = 1 if num_turns % 2 == 0 else 2

        if mode == "ai_vs_ai":
            values = ai_move(values, current_player)
            time.sleep(1)
        elif mode == "human_vs_ai":
            if current_player == 1:
                values = human_move(values, current_player)
            else:
                values = ai_move(values, current_player)

        print_board(values)
        state = check_winner(values)

        if state == 3:
            print("\nIt's a tie!")
            break
        elif state == 1:
            print("\nX wins!" + (" (You!)" if mode == "human_vs_ai" else ""))
            break
        elif state == 2:
            print("\nO wins!" + (" (AI!)" if mode == "human_vs_ai" else ""))
            break

        num_turns += 1


if __name__ == '__main__':
    main()
