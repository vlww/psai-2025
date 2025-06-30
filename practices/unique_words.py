import argparse 
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", type=str, help="Sentence to be split into unique words")
    args = parser.parse_args()
    words = split(args.sentence)
    words = unique(words)
    print(words)
    
def split(word):
    return re.split(r'[^a-zA-Z]+', word)

def unique(words):
    unique_words = set()
    for word in words:
        if word:
            unique_words.add(word.lower())
    return unique_words

if __name__ == "__main__":
    main()