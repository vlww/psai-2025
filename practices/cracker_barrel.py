import argparse
import time

def cracker_barrel(board, size, path=None):
    time.sleep(.05)
    if path is None:
        path = [board]

    peg_count = count_pegs(board)
    print(f"Depth: {len(path)}, Pegs left: {peg_count}")
    print_state(board, size)
    print()

    if peg_count == 1:
        print("Solution found!")
        time.sleep(2)
        for step, state in enumerate(path):
            time.sleep(1)
            print(f"Step {step}:")
            print_state(state, size)
            print()
        return True

    states = possible_states(board)
    print(f"Number of possible next states: {len(states)}")

    if not states:
        print("Dead end reached, backtracking...")
        return False

    for next_board in states:
        if next_board not in path:  # avoid cycles
            if cracker_barrel(next_board, size, path + [next_board]):
                return True  # propagate success

    return False


def count_pegs(board):
    return sum(board)

def print_state(board, size):
    position = 0
    for i in range(1, size+1):
        print(" "*(size-i), end="")
        for j in range(i):
            if board[position] == 0:
                print("O ", end="")
            if board[position] == 1:
                print("# ", end="")
            position += 1
        print()

def possible_states(board):
    jump_map = {
        0: [3, 5],
        1: [6, 8],
        2: [7, 9],
        3: [0, 5, 10, 12],
        4: [11, 13],
        5: [0, 3, 12, 14],
        6: [1, 8],
        7: [2, 9],
        8: [1, 6],
        9: [2, 7],
        10: [3, 12],
        11: [4, 13],
        12: [3, 5, 10, 14],
        13: [4, 11],
        14: [5, 12]
    }

    middle_map = {
    (0, 3): 1,
    (0, 5): 2,
    (1, 6): 3,
    (1, 8): 4,
    (2, 7): 4,
    (2, 9): 5,
    (3, 0): 1,
    (3, 5): 4,
    (3, 10): 6,
    (3, 12): 7,
    (4, 11): 7,
    (4, 13): 8,
    (5, 0): 2,
    (5, 3): 4,
    (5, 12): 8,
    (5, 14): 9,
    (6, 1): 3,
    (6, 8): 7,
    (7, 2): 4,
    (7, 9): 8,
    (8, 1): 4,
    (8, 6): 7,
    (9, 2): 5,
    (9, 7): 8,
    (10, 3): 6,
    (10, 12): 11,
    (11, 4): 7,
    (11, 13): 12,
    (12, 3): 7,
    (12, 5): 8,
    (12, 10): 11,
    (12, 14): 13,
    (13, 4): 8,
    (13, 11): 12,
    (14, 5): 9,
    (14, 12): 13
    }

    next_states = []

    for start_pos, possible_ends in jump_map.items():
        for end_pos in possible_ends:
            middle_pos = middle_map.get((start_pos, end_pos))
            if middle_pos is None:
                continue

            if board[start_pos] == 1 and board[middle_pos] == 1 and board[end_pos] == 0:
                print(f"Valid move: {start_pos} -> {end_pos} over {middle_pos}")
                new_board = board.copy()
                new_board[start_pos] = 0
                new_board[middle_pos] = 0
                new_board[end_pos] = 1
                next_states.append(new_board)

    return next_states


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs="+", type=int, help='The starting configuration, in 1s and 0s, separated by spaces')
    args = parser.parse_args()
    board = args.nums

    if len(board) != 15:
        print("Error: You must provide exactly 15 numbers representing the board!")
        return

    print("Starting board:")
    print_state(board, 5)
    print()

    solved = cracker_barrel(board, 5)
    if not solved:
        print("No solution found.")


if __name__ == "__main__":
    main()