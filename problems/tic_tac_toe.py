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
            for j in range(1,3):
            #check each row
                if all(state[i,:]==j):
                    return True, j
            #check each column
                if all(state[:,i]==j):
                    return True, j   
        flipped_diagonal = np.diag(np.fliplr(state))
        for j in range(1,3):
            #diagonals
            if all(state.diagonal() == j):
                return True, j
            if all(flipped_diagonal == j):
                return True, j
        #check for draw
        if not any(state==0):
            return True, 0
        return False, None
    
    def utility(self, state):
        terminal, winner = self.is_terminal(state)
        if not terminal:
            return 0
        if winner == 1:
            return 10
        return -10