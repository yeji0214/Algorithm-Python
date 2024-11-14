# 브루트포스
def dfs(n, sm):
    global ans
    if n >= N:
        ans = max(ans, sm)
        return

    # 상담 O
    if n + T[n] <= N:
        dfs(n + T[n], sm + P[n])
    # 상담 X
    dfs(n + 1, sm)

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)


# DP
N = int(input())
T = [0] * N
P = [0] * N
dp = [0] * (N + 1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

for n in range(N - 1, -1, -1):
    if n + T[n] <= N:
        dp[n] = max(dp[n + 1], P[n] + dp[n + T[n]])
    else:
        dp[n] = dp[n + 1]

print(dp[0])