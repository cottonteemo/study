a= int(input())

for i in range(a):
    x, y = map(int, input().split())
    length = y-x
    if length <= 2:
        print(1)
    else:
        Q = -1
        base = 1
        while True:
            if length <= 2* base + Q + 2:
                break
            else:
                base = base * (Q + 3 + 1) / (Q + 2)
                Q += 1
        k = Q + 2
        n = length - 2 * base +  k
        if n == 0:
            print(2*k-1)
        elif n <= k:
            print(2*k)
        else:
            print(2*k+1)
