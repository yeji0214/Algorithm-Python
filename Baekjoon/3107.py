address = input()
cut = address.split(':')

res = []

if len(cut) == 8:
    for c in cut:
        res.append(c.zfill(4))

else:
    if cut[0] == '':
        cut.pop(0)
    if cut[-1] == '':
        cut.pop(-1)

    zero = 8 - (len(cut) - 1)

    for c in cut:
        if c == '':
            for _ in range(zero):
                res.append('0000') 
        else:
            res.append(c.zfill(4))

print(*res, sep=':')