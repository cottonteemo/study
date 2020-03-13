import sys

x, y, w, h = map(int, sys.stdin.readline().split())
S1 = [x, y]
S2 = [[0, w], [0, h]]
S3 = [S1[0]-S2[0][0], S2[0][1]-S1[0], S1[1]-S2[1][0], S2[1][1]-S1[1]]

print(min(S3))


