# 그래프, bfs
from collections import deque

def bfs():
    q = deque()
    for i in range(len(tomato_index)):
        q.append((tomato_index[i][0], tomato_index[i][1]))

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[cx][cy] + 1
                q.append((nx, ny))


M, N = map(int, input().split()) # 가로, 세로
tomato = [[]* M for _ in range(N)]
ans = 0
well_done = 0
not_well_done = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
tomato_index = []

for i in range(N):
    tomato[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            tomato_index.append([i,j])

bfs()

for i in range(N):
    ans = max(ans, max(tomato[i])-1)
    not_well_done += tomato[i].count(0)
    if not_well_done > 0:
        ans = -1
        break

print(ans)