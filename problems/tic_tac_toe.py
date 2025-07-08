import numpy as np

class TicTacToeProblem:
    def __init__(self):
        self.initial_state = np.zeros((3, 3), dtype=int)

    def get_moves(self, state, player):
        return [(int(i), int(j)) for i, j in zip(*np.where(state == 0))]


    def get_successors(self, state, player):
        successors = []
        for move in self.get_moves(state, player):
            new_state = state.copy()
            new_state[move] = player
            successors.append((move, new_state))
        return successors

    def is_terminal(self, state):
        for p in [1, 2]:
            for i in range(3):
                if np.all(state[i, :] == p) or np.all(state[:, i] == p):
                    return True, p
            if np.all(np.diag(state) == p) or np.all(np.diag(np.fliplr(state)) == p):
                return True, p
        if not np.any(state == 0):
            return True, 0
        return False, None

    def utility(self, state):
        terminal, winner = self.is_terminal(state)
        if not terminal:
            return 0
        return 10 if winner == 1 else -10 if winner == 2 else 0
