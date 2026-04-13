N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_g, max_g = 256, 0
min_t = float('inf')
ans = 0

for g in ground:
    min_g = min(min_g, min(g))
    max_g = max(max_g, max(g))

for h in range(max_g, min_g - 1, -1):
    add, remove = 0, 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] > h:
                remove += (ground[i][j] - h)
            else:
                add += (h - ground[i][j])

    if add <= B + remove:
        t = add + (remove * 2)
        if t < min_t:
            min_t = t
            ans = h
    
print(min_t, ans)