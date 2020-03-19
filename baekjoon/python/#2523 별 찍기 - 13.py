a = int(input())
n = 0
while True:
    n += 1
    if n < a+1:
        print('*' * n)
    else:
        print('*' * (2*a-n))
    if n == 2*a -1:
        break
