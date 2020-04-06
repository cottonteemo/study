import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    c = [a, b]
    l.append(c)

l = sorted(l, key = lambda x: (x[1], x[0]))

for i in l:
    for k in i:
        print(k, end= ' ')
    print()