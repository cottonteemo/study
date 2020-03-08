Case = int(input())
mult = 1
for i in range(Case):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    else:
        for j in range(k):
            mult = mult * ((j+n+1) / (j+2))
        print(round(n * mult))
    mult = 1