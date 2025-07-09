import copy
import random
import time

ACTIONS = ['up', 'down', 'left', 'right']
GAMMA = 0.9
THRESHOLD = 1e-3 

class State:
    def __init__(self, reward):
        self.reward = reward
        self.value = 0.0

def get_next_state_coords(i, j, action, rows, cols):
    if action == 'up' and i > 0:
        return i - 1, j
    elif action == 'down' and i < rows - 1:
        return i + 1, j
    elif action == 'left' and j > 0:
        return i, j - 1
    elif action == 'right' and j < cols - 1:
        return i, j + 1
    return i, j  # if out of bounds, stay in same state

def value_iteration(matrix):
    rows, cols = len(matrix), len(matrix[0])
    states = [[State(matrix[i][j]) for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] in [100, -100]:
                states[i][j].value = matrix[i][j]

    iteration = 0

    while True:
        iteration += 1
        delta = 0
        new_values = copy.deepcopy([[s.value for s in row] for row in states])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] in [100, -100]: 
                    continue

                best_value = float('-inf')

                for action in ACTIONS:
                    expected_value = 0
                    for possible_action in ACTIONS:
                        prob = 0.8 if possible_action == action else 0.2 / 3
                        n1, n2 = get_next_state_coords(i, j, possible_action, rows, cols)
                        reward = matrix[n1][n2]
                        if matrix[n1][n2] in [100, -100]:
                            expected_value += prob * matrix[n1][n2]  
                        else:
                            expected_value += prob * (matrix[n1][n2] + GAMMA * states[n1][n2].value)


                    best_value = max(best_value, expected_value)

                delta = max(delta, abs(states[i][j].value - best_value))
                new_values[i][j] = best_value

        # Update values after computing everything
        for i in range(rows):
            for j in range(cols):
                states[i][j].value = new_values[i][j]

        time.sleep(.5)
        print(f"\nIteration {iteration}:")
        for row in states:
            print(['{0:6.2f}'.format(s.value) for s in row])

        if delta < THRESHOLD:
            break

def main():
    matrix = [[0, 0, 0, 100],
              [0, -100, 0, 0],
              [0, 0, -10, 0],
              [0, 0, 0, 0]]

    value_iteration(matrix)

if __name__ == '__main__':
    main()
