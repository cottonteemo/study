import sys

a, b = map(int, sys.stdin.readline().split())
c = [i for i in range(a)]

for i in range(a):
    line = list(str(sys.stdin.readline()))
    c[i] = line[0:b]

Examination = []
case_1 = 'WBWBWBWB'
case_2 = 'BWBWBWBW'

C1 = (case_1 + case_2) * 4
C2 = (case_2 + case_1) * 4

for y in range(a-7):
    for x in range(b-7):
        l = ''
        count1 = 0
        count2 = 0
        for k in range(y, y+8):
            l += ''.join(c[k][x:x+8])
        for i in range(len(l)):
            if l[i] != C1[i]:
                count1 += 1
        for i in range(len(l)):
            if l[i] != C2[i]:
                count2 += 1
        if count1 > count2:
            Examination.append(count2)
        else:
            Examination.append(count1)

print(min(Examination))