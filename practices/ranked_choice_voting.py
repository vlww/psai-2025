def read(filename):
    votes = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                row = line.strip().split(',')
                votes.append([int(x.strip()) for x in row])
    return votes

def firsts(votes, active_candidates):
    listt = {}
    for candidate in active_candidates:
        listt[candidate] = 0

    for vote in votes:
        for preference in vote:
            if preference in active_candidates:
                listt[preference] += 1
                break
    return listt

def printout(tally, total_votes):
    for candidate in sorted(tally):
        percent = 100 * tally[candidate] / total_votes
        print(f"{candidate}: {percent:.2f}%")
    print()

def whowins(tally, total_votes):
    for candidate in tally:
        if tally[candidate] > total_votes / 2:
            return candidate
    return None

def main(filename):
    try:
        votes = read(filename)
        total_voters = len(votes)
        stillin = []
        for vote in votes:
            for c in vote:
                if c not in stillin:
                    stillin.append(c)
        stillin.sort()

        round_num = 1
        while True:
            print(f"round {round_num}")
            tally = firsts(votes, stillin)
            printout(tally, total_voters)

            winner = whowins(tally, total_voters)
            if winner is not None:
                print(f"Winner: {winner}")
                break

            min_votes = min(tally[c] for c in stillin)
            lowest_candidates = [c for c in stillin if tally[c] == min_votes]

            if len(lowest_candidates) == len(stillin):
                print("Draw between: ", end="")
                for guy in stillin:
                    print(guy, "", end="")
                print()

                break

            to_eliminate = lowest_candidates[0]
            stillin.remove(to_eliminate)
            for vote in votes:
                if to_eliminate in vote:
                    vote.remove(to_eliminate)

            for vote in votes:
                if to_eliminate in vote:
                    vote.remove(to_eliminate)

            round_num += 1
    except Exception as e:
        print(f"Failed to process file '{filename}': {e}")

if __name__ == '__main__':
    main('practices/votes.txt')