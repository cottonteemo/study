a = int(input())
b = int(input())

l = []

if b <= 2:
    print(-1)
else:
    for i in range(a,b+1):
        l.append(i)
    for i in range(a,b+1):
        for j in range (2,i):
            if i % j == 0:
                l.remove(i)
                break
    if 1 in l:
        l.remove(1)
    if l == []:
        print(-1)
    else:
        print(sum(l))
        print(min(l))