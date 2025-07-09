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

def random_walk():
    position = 0
    for _ in range(100):
        if random.random() > 0.5:
            position += 1
        else:
            position -= 1
    return position

def random_walker(trials):
    total = 0
    for i in range(trials):
        total += random_walk()
    return total / trials

def main():
    outer_runs = 1000
    inner_trials = 1000

    average_positions = []
    for i in range(outer_runs):
        avg = random_walker(inner_trials)
        average_positions.append(avg)

    plt.hist(average_positions, bins=30, edgecolor='black')
    plt.title('plot')
    plt.xlabel('position')
    plt.ylabel('freq')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()