import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    a, b = sys.stdin.readline().split()
    c = [a, b]
    l.append(c)

l = sorted(l, key = lambda x: int(x[0]))

for i in range(n):
    print(l[i][0], l[i][1])