import sys

a = int(sys.stdin.readline())
L = [int(sys.stdin.readline()) for k in range(a)]
list = []

while True:
    if len(list) == a:
        break
    list.append(min(L))
    L.remove(min(L))

for i in list:
    print(i)
