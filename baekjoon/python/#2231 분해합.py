n = int(input())
a = n
digit = 1

while True:
    if a // 10 == 0:
        break
    else:
        a = a / 10
        digit += 1

Answer = 0

for i in range(n-digit*9,n):
    if i < 1:
        continue
    else:
        l = []
        for k in str(i):
            l.append(int(k))
        if i + sum(l) == n:
            Answer = 1
            print(i)
            break

if Answer == 0:
    print(0)
else:
    None