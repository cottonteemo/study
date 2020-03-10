import math

a, b = map(int, input().split())
for i in range(a,b+1):
    temp = 1
    n = int(math.sqrt(i))
    for j in range(2,n+1):
        if i % j == 0:
            temp *= 0
            break
    if temp ==1 and i > 1:
        print(i)
