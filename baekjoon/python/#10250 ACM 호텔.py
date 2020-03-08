a = int(input())

for i in range(a):
    H, W, C = map(int, input().split())
    if C % H == 0:
        Room = C//H
        Floor = H * 100
    else:
        Room = (C // H) + 1
        Floor = (C % H) * 100
    print(Floor + Room)