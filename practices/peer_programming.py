import argparse

def find_index(l):
    splitter, m = l.rsplit(" ", 1)
    clean = splitter.strip("[]")
    stuff = clean.split(",")
    listt = [int(item.strip()) for item in stuff if item.strip() != '']  # Remove blanks
    n = int(m.strip())

    for i in range(len(listt)):
        if listt[i] == n:
            print(i)
            return i
    print(-1)
    return -1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()
    find_index(args.s)
