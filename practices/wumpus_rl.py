import numpy as np
import itertools

# Variables
V = np.zeros((4, 4))
A = [(1, 0), (-1, 0), (0, 1), (0, -1)]
threshold = 0.01
discount_rate = 0.9

# Helper function
def get_neighbors(state, size, A):
    neighbors = []
    for a in A:
        new_state = tuple(np.array(state) + np.array(a))
        if 0 <= new_state[0] < size and 0 <= new_state[1] < size:
            neighbors.append(new_state)
    return neighbors

# Wall Probs
T = {}
for i in range(4):
    for j in range(4):
        state = (i, j)
        for a in A:
            new_state = tuple(np.add(np.array(state), np.array(a)))
            if not (0 <= new_state[0] < 4 and 0 <= new_state[1] < 4):
                T[(state, a, state)] = 0.99
                for neighbor in get_neighbors(state, 4, A):
                    T[(state, a, neighbor)] = 0.01 / len(get_neighbors(state, 4, A))
            else:
                T[(state, a, new_state)] = 0.8
                for neighbor in get_neighbors(state, 4, A):
                    if neighbor != new_state:
                        T[(state, a, neighbor)] = 0.2 / (len(get_neighbors(state, 4, A)) - 1)

# Rewards
def get_reward(state):
    if state == (1, 2):
        return -10
    if state == (2, 1):
        return -100
    if state == (3, 3):
        return 100
    return 0

# Value iteration
iteration_count = 0
while True:
    max_delta = 0
    new_V = np.copy(V)
    for state in itertools.product(range(4), range(4)):
        if state == (3, 3):
            continue  

        action_values = []
        for a in A:
            expected_value = 0
            for neighbor in get_neighbors(state, 4, A):
                P = T.get((state, a, neighbor), 0)
                R = get_reward(neighbor)
                expected_value += P * (R + discount_rate * V[neighbor])
            action_values.append(expected_value)
        best_value = max(action_values)
        new_V[state] = best_value
        max_delta = max(max_delta, abs(V[state] - best_value))

    V = new_V
    iteration_count += 1
    print(f"\nAfter iteration {iteration_count}:")
    print(np.round(V, 2))

    if max_delta < threshold:
        break
