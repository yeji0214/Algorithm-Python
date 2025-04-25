N, K = map(int, input().split())
ans = K

for i in range(N - 1):
    ans //= 2

print(ans)