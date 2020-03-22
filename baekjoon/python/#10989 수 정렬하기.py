import sys

a = int(sys.stdin.readline())
num_list = [0] * 10001

for i in range(a):
    b = int(sys.stdin.readline())
    num_list[b] += 1

for i in range(10001):
    if num_list[i] != 0:
        for k in range(num_list[i]):
            print(i)
    else:
        pass