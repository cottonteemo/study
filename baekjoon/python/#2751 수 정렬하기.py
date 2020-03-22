import sys

def merge(a, b):
    i = 0
    j = 0
    l = []
    while True:
        if a[i] > b[j]:
            l.append(b[j])
            j = j+1
        else:
            l.append(a[i])
            i = i+1
        if i == len(a):
            l = l + b[j:]
        elif j == len(b):
            l = l + a[i:]
        if len(l) == len(a) + len(b):
            break
    return l


def sort(x):
    if len(x) <= 1:
        return x
    else:
        p = len(x) // 2
        Left = sort([x[i] for i in range(p)])
        Right = sort([x[i] for i in range(p,len(x))])
        return merge(Left, Right)

a = int(sys.stdin.readline())
L =[int(sys.stdin.readline()) for k in range(a)]

for i in sort(L):
    print(i)