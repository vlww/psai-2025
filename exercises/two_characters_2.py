import argparse

def two_characters(s):
    unique_list = unique(s)
    max = 0
    for i in range(len(unique_list)):
        for j in range(i+1,len(unique_list)):
            keepers = []
            keepers.append(unique_list[i])
            keepers.append(unique_list[j])

            length = 0
            first = True
            for c in s:
                if c == keepers[0] and first == True:
                    length += 1
                    first = False
                if c == keepers[1] and first == False:
                    length += 1
                    first = True

            if length>max:
                max = length

            length = 0
            first = True
            for c in s:
                if c == keepers[1] and first == True:
                    length += 1
                    first = False
                if c == keepers[0] and first == False:
                    length += 1
                    first = True

            if length>max:
                max = length
            
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