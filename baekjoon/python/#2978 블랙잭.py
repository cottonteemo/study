import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
L = []
breaker = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            Sum = l[i] + l[j] + l[k]
            if Sum == m:
                L.append(Sum)
                break
            elif Sum < m:
                L.append(Sum)
            else:
                continue
        if breaker == 1:
            break
    if breaker == 1:
        break
if len(L) > 0:
    print(max(L))