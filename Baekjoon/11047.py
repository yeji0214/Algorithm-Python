N, K = map(int, input().split())
A = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0

for i in A:
    if i <= K:
        ans += K // i
        K %= i

print(ans)