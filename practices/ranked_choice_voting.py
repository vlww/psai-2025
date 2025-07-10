def read(filename):
    votes = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                row = line.strip().split(',')
                vote = []
                for item in row:
                    equals = [x.strip() for x in item.strip().split('=') if x.strip()]
                    if equals:
                        vote.append(equals)
                votes.append(vote)
    return votes

def firsts(votes, active_candidates):
    tally = {c: 0 for c in active_candidates}

    for vote in votes:
        for group in vote:
            valid = [c for c in group if c in active_candidates]
            if valid:
                weight = 1.0 / len(valid)
                for c in valid:
                    tally[c] += weight
                break  # stop at first active group
    return tally

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

        # Build list of all candidates
        stillin = []
        for vote in votes:
            for group in vote:
                for c in group:
                    if c not in stillin:
                        stillin.append(c)
        stillin.sort()

        round_num = 1
        while True:
            # Filter out exhausted ballots (no active candidates left)
            active_votes = []
            for vote in votes:
                found = False
                for group in vote:
                    if any(c in stillin for c in group):
                        found = True
                        break
                if found:
                    active_votes.append(vote)

            total_voters = len(active_votes)
            print(f"Round {round_num}")
            tally = firsts(active_votes, stillin)
            printout(tally, total_voters)

            winner = whowins(tally, total_voters)
            if winner is not None:
                print(f"Winner: {winner}")
                break

            min_votes = min(tally[c] for c in stillin)
            lowest_candidates = [c for c in stillin if tally[c] == min_votes]

            if len(lowest_candidates) == len(stillin):
                print("Draw between: ", " ".join(stillin))
                break

            to_eliminate = lowest_candidates[0]
            stillin.remove(to_eliminate)

            for vote in votes:
                for group in vote:
                    if to_eliminate in group:
                        group.remove(to_eliminate)

            round_num += 1
    except Exception as e:
        print(f"Failed to process file '{filename}': {e}")

if __name__ == '__main__':
    main('practices/votes_cleaned.txt')
