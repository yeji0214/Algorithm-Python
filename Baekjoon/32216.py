n, k, t = map(int, input().split())
D = list(map(int, input().split()))
ans = 0

for i in range(len(D)):
    if t < k:
        nt = t + D[i] + abs(t - k)
    elif t > k:
        nt = t + D[i] - abs(t - k)
    else:
        nt = t + D[i]

    ans += abs(nt - k)

print(ans)