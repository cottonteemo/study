import sys
import math

a = int(sys.stdin.readline())
A = []
B = []
for i in range(a):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if r1 - r2 >= 0:
            R1 = r1
            R2 = r2
        else:
            R1 = r2
            R2 = r1
        if R1 + R2 < d:
            print(0)
        elif R1 + R2 == d:
            print(1)
        elif R1 + R2 > d and d > R1 - R2:
            print(2)
        elif R1 - R2 == d:
            print(1)
        else:
            print(0)
