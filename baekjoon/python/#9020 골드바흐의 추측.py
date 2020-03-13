import sys
import math

l = [x for x in range(2,10001)]
for i in range(2, 10001):
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            l.remove(i)
            break
a = int(sys.stdin.readline())
for i in range(a):
    n = int(sys.stdin.readline())
    k = [x for x in l if x >= 1/2 * n and x < n]
    for j in k:
        if n - j in l:
            print(n-j, j)
            break