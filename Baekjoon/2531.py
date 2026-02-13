N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

cnt = [0] * (d + 1)
kind = 0

for i in range(k):
    x = sushi[i]
    if cnt[x] == 0:
        kind += 1
    cnt[x] += 1

ans = kind + (1 if cnt[c] == 0 else 0)

for s in range(1, N):
    out = sushi[s - 1]
    cnt[out] -= 1
    if cnt[out] == 0:
        kind -= 1

    inn = sushi[(s + k - 1) % N]
    if cnt[inn] == 0:
        kind += 1
    cnt[inn] += 1

    cur = kind + (1 if cnt[c] == 0 else 0)

    if cur > ans:
        ans = cur
        if ans == k + 1:
            break

print(ans)