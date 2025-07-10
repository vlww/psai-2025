def main(filename):
    try:
        with open(filename, 'r') as file:
            all_votes = []
            for line in file:
                line = line.strip()
                if line:
                    vote = [int(x.strip()) for x in line.split(',')]
                    all_votes.append(vote)

            for i, vote in enumerate(all_votes, 1):
                print(f"Voter {i}: {vote}")

    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return


if __name__ == '__main__':
    main('practices/votes.txt')
