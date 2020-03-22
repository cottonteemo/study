a = int(input())


l1 = []
l2 = []

for i in range(a):
    if i % 2 == 0:
        l1.append('*')
        l1.append(' ')
    else:
        l2.append(' ')
        l2.append('*')


for i in range(a):
    print(''.join(l1))
    print(''.join(l2))