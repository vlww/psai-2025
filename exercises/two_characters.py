import argparse

def two_characters(s):
    unique_list = unique(s)
    max = 0
    for i in range(len(unique_list)):
        for j in range(i+1,len(unique_list)):
            keepers = set()
            keepers.add(unique_list[i])
            keepers.add(unique_list[j])
            
            just_keepers_string = ""
            for c in s:
                if c in keepers:
                    just_keepers_string += c

            if check_is_alternating(just_keepers_string):
                if len(just_keepers_string)>max:
                    max = len(just_keepers_string)
            
    return max

def unique(s):
    unique_list = []
    uniques = set()
    for c in s:
        if c not in uniques:
            uniques.add(c)
            unique_list.append(c)
    return unique_list

def check_is_alternating(s):
    char1 = s[0]
    char2 = s[1]
    for c in range(len(s)):
        if c%2==0:
            if s[c] != char1:
                return False
        else:
            if s[c] != char2:
                return False
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()
    print(two_characters(args.s))