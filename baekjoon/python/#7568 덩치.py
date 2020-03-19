import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append([a,b])

Rank = []
for i in l:
    count = 1
    for k in l:
        if k[0] > i[0] and k [1] > i[1]:
            count += 1
    Rank.append(count)

for i in Rank:
    print(i, end=' ')
