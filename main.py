import random

rows = 4
columns = 4

arr = [[0 for i in range(rows)] for i in range(columns)]

def number_to_idx(num):
    num -= 1
    x, y = num//rows, num%4
    print(x, y)

def idx_to_number(x, y):
    return x * rows + y + 1

def rand_number_input(x, y):
    rnum = random.random()
    arr[x][y] = 2 if rnum <= 0.75 else 4

def array_print():
    print("-"*7)
    for i in range(rows):
        print(*arr[i])
    print("-"*7)

def get_empty_list():
    empty = []
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == 0:
                empty.append(idx_to_number(i, j))
    print(*empty)

if __name__ == "__main__":
    arr[0][2] = 4
    arr[3][1] = 2
    array_print()
    get_empty_list()