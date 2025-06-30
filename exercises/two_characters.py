import argparse

def two_characters(s):
    'write your code here'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()
    print(two_characters(args.s))