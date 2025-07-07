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
        states, actions = [], []
        for move in self.get_moves(state,player):
            new_state = state.copy()
            new_state[move[0], move[1]] = player
            states.append(new_state)
            actions.append(move)
        return states, actions
    

    def is_terminal(self, state):
        for i in range(3):
        #check each row
            if all(state[i,:]==1) or all(state[i,:]==2):
                return True
        #check each column
            if all(state[:,i]==1) or all(state[:,i]==2):
                return True
        #diagonals
        flipped_diagonal = np.diag(np.fliplr(state))
        if all(state.diagonal() == 1) or all(state.diagonal() == 2):
            return True
        if all(flipped_diagonal == 1) or all(flipped_diagonal == 2):
            return True
        #check for draw
        if not any(state==0):
            return True
        return False