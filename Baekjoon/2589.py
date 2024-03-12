# 그래프, bfs
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    distance = 0

    temp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and map[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                distance = temp[cx][cy] + 1
                temp[nx][ny] = distance
                q.append((nx, ny))

    return distance

N, M = map(int, input().split())
map = [[] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for i in range(N):
    map[i] = list(input())
    
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L': # 육지 발견
            ans = max(bfs(i, j), ans)

print(ans)