# 그래프, bfs
from collections import deque

def bfs(x, y):
    size = 0 # 현재 음식물의 크기
    visited[x][y] = True
    q = deque()

    if arr[x][y] == 1: # 음식물인 경우
        q.append((x,y))
        size += 1
    
    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]: # 범위를 벗어났거나 이미 방문한 곳인 경우
                continue

            visited[nx][ny] = True

            if arr[nx][ny] == 1: # 음식물인 경우
                size += 1
                q.append((nx, ny))

    return size


N, M, K = map(int, input().split())

arr = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
food_waste = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j]: # 방문하지 않은 곳
            food_waste = max(food_waste, bfs(i, j))

print(food_waste)