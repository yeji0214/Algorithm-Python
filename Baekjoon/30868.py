T = int(input())
for _ in range(T):
    n = int(input())
    res = []
    n1, n2 = n // 5, n % 5
    for _ in range(n1):
        res.append('++++')
    if n2 > 0:
        res.append('|' * n2)

    print(' '.join(res))