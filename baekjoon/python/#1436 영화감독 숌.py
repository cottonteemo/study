a = int(input())

count = 0
num = 666
while True:
    Num = str(num)
    if '666' in Num:
        count += 1

    if count == a:
        print(Num)
        break

    num = num + 1
