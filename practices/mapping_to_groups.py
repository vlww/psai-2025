import argparse
import math

class Student:
    def __init__(self, role):
        self.role = role

def main(N, M, K):
    students = []

    for i in range(N):
        if (i<M):
            students.append(Student("scribe"))
        else:
            students.append(Student("director"))

    solution = backtrack(students, K)

    if solution:
        for i, group in enumerate(solution):
            print(f"Group {i + 1}: {[student.role for student in group]}")
    else:
        print("No valid group assignment found.")

def backtrack(students, K, groups=None, index=0):
    if groups is None:
        groups = [[] for _ in range(K)]

    max_group_size = math.ceil(len(students) / K)


    if index == len(students):
        if check(groups):
            return groups  
        return None

    group_indices = sorted(range(K), key=lambda i: len(groups[i]))

    for i in group_indices:
        if len(groups[i]) >= max_group_size:
            continue

        groups[i].append(students[index])
        result = backtrack(students, K, groups, index + 1)
        if result:
            return result
        groups[i].pop()  # backtrack

    return None

def check(groups):
    good = True
    for i, group in enumerate(groups):
        has_scribe = any(student.role == "scribe" for student in group)
        if not has_scribe:
            good = False
    return good

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Number of students')
    parser.add_argument('M', type=int, help='Number of scribes')
    parser.add_argument('K', type=int, help='Number of groups')
    args = parser.parse_args()
    main(args.N, args.M, args.K)