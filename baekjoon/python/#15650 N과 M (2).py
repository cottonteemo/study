import sys

n, m = map(int, sys.stdin.readline().split())
Array = [x for x in range(1,n+1)]
Set = []
a = 0
def recursive(idx, n, m, a):

    if len(Set) == m:
            for w in Set:
                print(w, end=' ')
            print()

    else:
        for i in range(a,n):
            if Array[i] in Set:
                continue
            else:
                Set.append(Array[i])
                a = Array[i]
                recursive(idx+1, n, m, a)
                Set.remove(Array[i])

recursive(0, n, m, a)