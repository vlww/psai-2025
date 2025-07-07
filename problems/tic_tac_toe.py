import numpy as np

class TicTacToeProblem:
    def __init__(self):
        self.initial_state = np.zeros((3,3))

    def get_moves(self, state, player):
        raw_moves = np.where(state == 0)
        moves = []
        for i, j in zip(*raw_moves):
            moves.append((i, j))
        return moves


    def get_successors(self, state, player):
        pass