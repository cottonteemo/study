a = int(input())
n = a

for i in range(2*a+1):
    if n-i > 0:
        print(i * ' ' + '*' *(2*(n-i) -1))
    elif n == i:
        pass
    elif n-i<-1:
        print((2*a-i) * ' ' + '*' * (2*(i-n)-1))
    elif n-i == -2*a:
        break

