import sys

column = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = [(x, y) for x in range(9) for y in range(9) if column[x][y] == 0]

def recursive(idx):

    if idx == len(blank):
        for c in column:
            print(*c)
        print()
        sys.exit()

    x = blank[idx][0]
    y = blank[idx][1]

    dx = x // 3 * 3
    dy = y // 3 * 3

    num_list = [0] + [1] * 9

    for i in range(9):
        if column[x][i] > 0:
            num_list[column[x][i]] = 0
        if column[i][y] > 0:
            num_list[column[i][y]] = 0

    for i in range(dx, dx + 3):
        for j in range(dy, dy + 3):
            if column[i][j] > 0:
                num_list[column[i][j]] = 0

    candidate = []
    for i in range(len(num_list)):
        if num_list[i] == 1:
            candidate.append(i)

    for num in candidate:
        column[x][y] = num
        recursive(idx + 1)
        column[x][y] = 0

recursive(0)