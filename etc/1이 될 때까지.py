N, K = map(int, input().split())
ans = 0

while N > 1:
    if N % K != 0:
        N -= 1
        ans += 1
    else:
        N //= K
        ans += 1

print(ans)