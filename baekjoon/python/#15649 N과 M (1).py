import sys

n,m = map(int, sys.stdin.readline().split())
Array = [x for x in range(1,n+1)]
set = []

def recursive(idx, n, m):
    if idx == m:
        for w in set:
            print(w, end=' ')
        print()
        return

    for i in Array:
        if i in set:
            continue
        else:
            set.append(i)
            recursive(idx+1, n, m)
            set.remove(i)

recursive(0, n, m)

