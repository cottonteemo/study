import sys

l= [0, 0, 0, [0, 0]]
for i in range(3):
    a, b = list(map(int, sys.stdin.readline().split()))
    l[i] = [a, b]
S1 = [l[i][0] for i in range(len(l))]
S2 = [l[i][1] for i in range(len(l))]

for i in S1:
    if S1.count(i) == 1:
        S1[3] = i
for i in S2:
    if S2.count(i) == 1:
        S2[3] = i
print(S1[3], S2[3])