def main(bag1, bag2, constraint):
    prune1 = []
    prune2 = []
    for i in bag1:
        possible = False
        for j in bag2:
            if (i+j) == constraint:
                possible = True
        if not possible:
            prune1.append(i)

    for i in bag2:
        possible = False
        for j in bag1:
            if (i+j) == constraint:
                possible = True
        if not possible:
            prune2.append(i)

    for i in prune1:
        bag1.remove(i)
    for i in prune2:
        bag2.remove(i)

    return bag1, bag2


    
    
if __name__ == "__main__":
    bag1 = [10, 5, 2, 3]
    bag2 = [10, 8, 15]
    constraint = 20
    print(main(bag1, bag2, constraint))