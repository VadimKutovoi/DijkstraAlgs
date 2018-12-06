import random

def print_header(name):
    line = "-" * 46
    print(line)
    print(" " * int((23 - len(name)/2)), name, " " * int((23 - len(name)/2)))
    print(line)


def print_separator():
    print("-" * 46)


def compare_lists(list1, list2):
    length = max(len(list1), len(list2))
    erc = 0
    for i in range(0, length):
        if list1[i] != list2[i]:
            erc += 1
    return erc


def generate_matrix(size):
    random.seed()
    MAX = 1000000
    matrix = [[0 for x in range(size)] for y in range(size)]
    j = 0
    for i in range(0, size):
        for k in range(j, size):
            if i == k:
                matrix[i][k] = MAX
            elif k % 3 == 0:
                matrix[i][k] = MAX
            elif k % 5 == 0:
                matrix[i][k] = MAX
            else:
                matrix[i][k] = random.randint(1, 10)
        j += 1

    for i in range(0, size):
        for k in range(0, size):
            matrix[k][i] = matrix[i][k]

    return matrix


