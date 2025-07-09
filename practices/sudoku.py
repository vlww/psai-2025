from collections import deque
import argparse
import copy
import time

class Node:
    def __init__(self, number, fixed=False):
        self.number = number
        self.fixed = fixed 

    def __repr__(self):
        return str(self.number) if self.number != 0 else '_'


def main(filename):
    try:
        with open(filename, 'r') as file:
            board = []

            for line in file:
                line = line.strip()
                row = []
                for char in line:
                    if char == '_':
                        row.append(Node(0))
                    elif char.isdigit():
                        row.append(Node(int(char), fixed=True))

                    else:
                        raise ValueError(f"Invalid character '{char}' in line: {line}")
                if len(row) != 9:
                    raise ValueError(f"Invalid row length: {row}")
                board.append(row)

            if len(board) != 9:
                raise ValueError(f"Expected 9 rows, got {len(board)}")

            print("Initial board:")
            print_state(board)

            domains = init_domains(board)
            solved = backtrack(board, domains)

            if solved:
                print("\ngg ez")
            else:
                print("im ahh")

    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return

def print_state(board):
    for row in board:
        for cell in row:
            if cell.number == 0:
                print("\033[90m_ \033[0m", end="")
            elif cell.fixed:
                print(f"\033[1m{cell.number} \033[0m", end="")  # blue
            else:
                print(cell.number, "", end="")  # white
        print()
    print()


def get_neighbors(pos):
    row, col = pos
    neighbors = set()

    for i in range(9):
        if i != col:
            neighbors.add((row, i))
        if i != row:
            neighbors.add((i, col))

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if (r, c) != pos:
                neighbors.add((r, c))
    return neighbors

def init_domains(board):
    domains = {}
    for r in range(9):
        for c in range(9):
            val = board[r][c].number
            if val != 0:
                domains[(r, c)] = {val}
            else:
                possible = set(range(1, 10))
                # Remove used numbers in row, col, box
                possible -= set(board[r][col].number for col in range(9) if board[r][col].number != 0)
                possible -= set(board[row][c].number for row in range(9) if board[row][c].number != 0)
                start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                for rr in range(start_row, start_row + 3):
                    for cc in range(start_col, start_col + 3):
                        val2 = board[rr][cc].number
                        if val2 != 0:
                            possible.discard(val2)
                domains[(r, c)] = possible
    return domains

def enforce_arc_consistency(domains, x1, x2):
    revised = False
    to_remove = set()
    for x in domains[x1]:
        if all(x == y for y in domains[x2]):
            to_remove.add(x)
    if to_remove:
        domains[x1] -= to_remove
        revised = True
    return revised

def AC3(domains):
    queue = deque()
    for x1 in domains:
        for x2 in get_neighbors(x1):
            queue.append((x1, x2))

    while queue:
        x1, x2 = queue.popleft()
        if enforce_arc_consistency(domains, x1, x2):
            if len(domains[x1]) == 0:
                return False 
            for xk in get_neighbors(x1):
                if xk != x2:
                    queue.append((xk, x1))
    return domains

def find_unassigned_cell(domains, board):
    unassigned = [(pos, d) for pos, d in domains.items() if board[pos[0]][pos[1]].number == 0]
    if not unassigned:
        return None
    unassigned.sort(key=lambda x: len(x[1]))
    return unassigned[0][0]

def backtrack(board, domains):
    cell = find_unassigned_cell(domains, board)
    if cell is None:
        return True 

    row, col = cell
    for val in sorted(domains[cell]):
        domains_copy = copy.deepcopy(domains)

        board[row][col].number = val
        domains[cell] = {val}

        result = AC3(domains)
        if result != False:
            # time.sleep(.1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print_state(board)

            if backtrack(board, domains):
                return True

        board[row][col].number = 0
        domains = domains_copy

    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='Path to file')
    args = parser.parse_args()
    main(args.file)
