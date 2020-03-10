a = int(input())
l = [2]
for i in range(3,a+1):
    l.append(i)
for i in range(3, a+1):
    for j in range (2,i):
        if i % j == 0:
            l.remove(i)
            break
print(l)

