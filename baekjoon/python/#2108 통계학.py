import sys
import collections

a = int(sys.stdin.readline())
l = sorted([int(sys.stdin.readline()) for k in range(a)])
AVG = round(sum(l) / len(l), 0)
MID = l[int((len(l)-1)/2)]
DIF = max(l) - min(l)
counter = sorted(list(collections.Counter(l).items()), key = lambda x: x[1], reverse = True)

if a > 1:
    k1 = list(counter[0])
    k2 = list(counter[1])
    if k1[1] == k2[1]:
        CNT = k2[0]
    else:
        CNT = k1[0]
else:
    CNT = MID

print('%.0f'%AVG)
print(MID)
print(CNT)
print(DIF)