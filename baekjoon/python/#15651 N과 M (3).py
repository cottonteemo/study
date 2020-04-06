import sys

n, m = map(int, sys.stdin.readline().split())
Array = [x for x in range(1,n+1)]
Set = []

def recursive(idx, n, m):

    if len(Set) == m:
        for w in Set:
            print(w, end=' ')
        print()

    else:
        for i in range(n):
            Set.append(Array[i])
            recursive(idx+1, n, m)
            del Set[idx]


recursive(0, n, m)

