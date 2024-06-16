# bfs
from collections import deque

def bfs(x, y):
    global ans

    ice[x][y] = -1
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0:
                q.append((nx, ny))
                ice[nx][ny] = -1
    ans += 1

N, M = map(int, input().split())
ice = [[]* M for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    ice[i] = list(map(int, input()))

for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            bfs(i, j)

print(ans)



# dfs

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if ice[x][y] == 0:
        ice[x][y] = 1
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


N, M = map(int, input().split())
ice = [[]* M for _ in range(N)]

for i in range(N):
    ice[i] = list(map(int, input()))

ans = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ans += 1

print(ans)