def spinner_world():
    probs = [0.5, 0.3, 0.2]
    outcomes = [1, 2, -1]
    expected = 0

    for p in range(len(probs)):
        expected += probs[p]*outcomes[p]

    return expected

def cursed_die():
    probs = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    outcomes = [1, 2, 3, 4, 5, -3]

    expected = 0

    for p in range(len(probs)):
        expected += probs[p]*outcomes[p]

    return expected


if __name__ == '__main__':
    print(spinner_world())
    print(cursed_die())
