import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.tic_tac_toe import TicTacToeProblem
from lib.minimax import MinimaxSolver

problem = TicTacToeProblem()
state = problem.initial_state.copy()
solver = MinimaxSolver(
    initial_state=state,
    get_successor_fn=problem.get_successors,
    is_terminal_fn=problem.is_terminal,
    utility_fn=problem.utility,
    max_depth=9
)

player = 1
turn = 0

while True:
    terminal, winner = problem.is_terminal(state)
    if terminal:
        print("\nGame Over!")
        print("Draw" if winner == 0 else f"Winner: Player {winner}")
        print(state)
        break

    print(f"\nTurn {turn}: Player {player}'s move")
    score, move = solver.minimax(state, player=player, depth=6)
    print(f"Best move: {move} (score: {score})")
    state[move] = player  # Apply move
    print(state)
    player = 2 if player == 1 else 1  # Switch turns
    turn += 1
