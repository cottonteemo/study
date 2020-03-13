import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    l = [a, b, c]
    if l == [0, 0, 0]:
        break
    else:
        k = max(l)
        l.remove(k)
        if l[0] **2 + l[1] **2 == k **2:
            print('right')
        else:
            print('wrong')

