# DP
N = int(input())
colors = []

for _ in range(N):
    colors.append(list(map(int, input().split())))

for i in range(1, N):
    colors[i][0] += min(colors[i-1][1], colors[i-1][2])
    colors[i][1] += min(colors[i-1][0], colors[i-1][2])
    colors[i][2] += min(colors[i-1][0], colors[i-1][1])

print(min(colors[N-1]))