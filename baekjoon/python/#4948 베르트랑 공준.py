import sys
import math


l = []
for i in range(2, 246912):
    temp = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            temp *= 0
            break
    if temp ==1:
        l.append(i)

while True:
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    for i in l:
        if i <= n:
            continue
        elif n < i <= 2*n:
            count += 1
        else:
            break
    print(count)


