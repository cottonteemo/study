def concatenate(r1, r2, r3):
    return [''.join(x) for x in zip(r1, r2, r3)]

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        TOP = concatenate(star(int(n/3)),star(int(n/3)),star(int(n/3)))
        MID = concatenate(star(int(n/3)), [' '*int(n/3)]*int(n/3), star(int(n/3)))
        BOT = concatenate(star(int(n/3)),star(int(n/3)),star(int(n/3)))

    return TOP + MID + BOT

n = int(input())
print('\n'.join(star(n)))