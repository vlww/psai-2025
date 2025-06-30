import argparse 
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", type=str, help="Sentence to be split into unique words")
    args = parser.parse_args()
    words = split(args.sentence)
    words = lower(words)
    words = unique(words)
    print(words)
    
def split(sentence):
    word_list = re.split(r'[^a-zA-Z]+', sentence)
    words = []
    for word in word_list:
        if word:
            words.append(word)
    return words

def lower(words):
    new_list = [0] * len(words)
    for i in range(len(words)):
        new_list[i] = words[i].lower()
    return new_list

def unique(words):
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            seen.add(word.lower())
            unique_words.append(word)
    return unique_words

if __name__ == "__main__":
    main()