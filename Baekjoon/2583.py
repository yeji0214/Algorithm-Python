# 그래프, bfs
from collections import deque

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    size = 0

    if arr[x][y] == 0:
        q.append((x,y))
        size += 1

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0:
                    size += 1
                    q.append((nx, ny))

    if size > 0:
        ans.append(size)

M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# for _ in range(K):
#     sx, sy, ex, ey = map(int, input().split())
#     nsx = sx; nsy = sy + (ey-sy-1); nex = ex-1; ney = (ey-1) - (ey-sy-1)
#     fsx = M-1-nsy; fsy = nsx; fex = M-1-ney; fey = nex

#     for i in range(fsx, fex+1):
#         for j in range(fsy, fey+1):
#             arr[i][j] = 1

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

print(len(ans))
print(*sorted(ans))