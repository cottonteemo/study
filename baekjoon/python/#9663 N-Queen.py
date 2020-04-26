import sys

n = int(sys.stdin.readline())
Array = [True] * n
Set = [True] * n
row = [True] * n
diag1 = [True] * (2 * n - 1)
diag2 = [True] * (2 * n - 1)
case = 0

def setting(idx, x, y):
    global Array

    if y == False:
        Array = [True] * n
        row[x] = False
        diag1[idx + x] = False
        diag2[x - idx + n - 1] = False
    else:
        row[x] = True
        diag1[idx + x] = True
        diag2[x - idx + n - 1] = True

    return(Array)

def recursion(idx, n):
    global case

    if idx == n:
        case += 1
        return

    for i in range(n):
        if diag1[idx + i] == False:
            continue
        if diag2[i-idx+n-1] == False:
            continue
        if row[i] == False:
            continue
        setting(idx, i, False)
        recursion(idx+1, n)
        setting(idx, i, True)


recursion(0, n)

print(case)