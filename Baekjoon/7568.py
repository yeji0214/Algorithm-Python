# 구현, 브루트포스
N = int(input())
weight = []
height = []
rank = []

for _ in range(N):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for i in range(N):
    cw = weight[i]
    ch = height[i]
    big = 0
    for j in range(N):
        if cw < weight[j] and ch < height[j]:
            big += 1
    rank.append(big + 1)

print(*rank)