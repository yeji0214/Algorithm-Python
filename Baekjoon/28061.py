N = int(input())
lemon = list(map(int, input().split()))
ans = 0

for i in range(N):
    ans = max(ans, lemon[i] - (N - i))

print(ans)