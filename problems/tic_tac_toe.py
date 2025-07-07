import numpy as np

class TicTacToeProblem:
    def __init__(self):
        self.initial_state = np.zeros((3,3))

    def get_moves(self, state, player):
        moves = np.where(state == 0)

    def get_successors(self, state, player):
        pass