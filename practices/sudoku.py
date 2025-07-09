from collections import deque
import copy
import time

class Node:
    def __init__(self, number):
        self.number = number

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
                        row.append(Node(int(char)))
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
                print_state(board)
                print("\ngg ez")
            else:
                print("im ahh")

    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return

def print_state(board):
    for r in board:
        print(" ".join(str(c) for c in r))
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

def enforce_arc_consistency(domains, xi, xj):
    revised = False
    to_remove = set()
    for x in domains[xi]:
        # If no y in xj's domain differs from x, remove x from xi
        if all(x == y for y in domains[xj]):
            to_remove.add(x)
    if to_remove:
        domains[xi] -= to_remove
        revised = True
    return revised

def AC3(domains):
    queue = deque()
    for xi in domains:
        for xj in get_neighbors(xi):
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()
        if enforce_arc_consistency(domains, xi, xj):
            if len(domains[xi]) == 0:
                return False  # failure
            for xk in get_neighbors(xi):
                if xk != xj:
                    queue.append((xk, xi))
    return domains

def find_unassigned_cell(domains, board):
    # MRV heuristic: cell with smallest domain > 1
    unassigned = [(pos, d) for pos, d in domains.items() if board[pos[0]][pos[1]].number == 0]
    if not unassigned:
        return None
    # Sort by domain size
    unassigned.sort(key=lambda x: len(x[1]))
    return unassigned[0][0]

def backtrack(board, domains):
    cell = find_unassigned_cell(domains, board)
    if cell is None:
        return True  # Solved

    row, col = cell
    for val in sorted(domains[cell]):
        # Make a copy of domains to restore later if needed
        domains_copy = copy.deepcopy(domains)

        # Assign value
        board[row][col].number = val
        domains[cell] = {val}

        # Run AC3 to propagate constraints
        result = AC3(domains)
        if result != False:
            time.sleep(.2)
            print_state(board)

            if backtrack(board, domains):
                return True

        # Backtrack
        board[row][col].number = 0
        domains = domains_copy

    return False

if __name__ == '__main__':
    main('practices/sudoku.txt')
