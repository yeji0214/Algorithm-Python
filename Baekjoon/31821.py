N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))
M = int(input())
ans = 0

for _ in range(M):
    ans += prices[int(input()) - 1]

print(ans)