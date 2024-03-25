# 구현, 시뮬레이션
H, W = map(int, input().split())
arr = [[0] * W for _ in range(H)]
height = list(map(int, input().split()))
ans = 0

for i in range(W):
    for j in range(H-height[i], H):
        arr[j][i] = 1

for i in range(H):
    block = []
    for j in range(W):
        if arr[i][j] == 1:
            block.append(j)
    if len(block) > 1:
        s = block.pop(0)
        e = block.pop(0)
        ans += e - s - 1

        while block:
            s = e
            e = block.pop(0)
            ans += e - s - 1

print(ans)