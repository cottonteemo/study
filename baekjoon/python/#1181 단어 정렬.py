import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    word = sys.stdin.readline()
    l.append(word[0:-1])

l = sorted(set(l), key = lambda x: (len(x), x))

for i in l:
    print(i)