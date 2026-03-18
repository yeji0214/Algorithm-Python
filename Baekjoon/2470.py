N = int(input())
S = sorted(list(map(int, input().split())))

current = float('inf')
s, e = 0, N - 1

while s < e:
    res = S[s] + S[e]
    c = abs(res - 0)

    if c < current:
        current = c
        ans = [S[s], S[e]]
        if res > 0:
            e -= 1
        else:
            s += 1
    else:
        if res > 0:
            e -= 1
        else:
            s += 1

print(*ans)