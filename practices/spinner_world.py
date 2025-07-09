def main():
    probs = [0.5, 0.3, 0.2]
    outcomes = [1, 2, -1]

    for p in range(len(probs)):
        expected += probs[p]*outcomes[p]

    return expected


if __name__ == '__main__':
    print(main())
