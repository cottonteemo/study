def F(n):
    if n < 2:
        if n < 1:
            return 0
        else:
            return 1
    else:
        return F(n-1) + F(n-2)

a = int(input())
print(F(a))