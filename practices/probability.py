import random
import matplotlib.pyplot as plt

def spinner_world():
    probs = [0.5, 0.3, 0.2]
    outcomes = [1, 2, -1]
    expected = sum(p * o for p, o in zip(probs, outcomes))
    return expected

def cursed_die():
    probs = [1/6] * 6
    outcomes = [1, 2, 3, 4, 5, -3]
    expected = sum(p * o for p, o in zip(probs, outcomes))
    return expected

def random_walker(trials):
    positions = []
    for i in range(trials):
        position = 0
        for j in range(1000):
            if random.random() > 0.5:
                position += 1
            else:
                position -= 1
        positions.append(position)
    return positions

if __name__ == '__main__':
    trials = 1000
    positions = random_walker(trials)

    plt.hist(positions, bins=30, edgecolor='black')
    plt.title(f'plot')
    plt.xlabel('position')
    plt.ylabel('freq')
    plt.grid(True)
    plt.show()
