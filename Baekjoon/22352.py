# 그래프, bfs
from collections import deque

def bfs(x, y):
    global change

    q = deque()
    q.append((x,y))
    visited[x][y] = True

    current = after[x][y] # 현재 영역의 값
    if before[x][y] != current: # 백신을 놓기 전과 후의 결과가 다를 때
        change += 1

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and before[x][y] == before[nx][ny]: # 범위 내, 방문하지 않은 곳, 인접한 영역
                visited[nx][ny] = True
                if current != after[nx][ny]:
                    return 'NO'
                q.append((nx, ny))


N, M = map(int, input().split())

before = [[] * M for _ in range(N)] # 백신을 놓기 전
after = [[] * M for _ in range(N)] # 백신을 놓은 뒤
visited = [[False] * M for _ in range(N)]
change = 0

for i in range(N):
    before[i] = list(map(int, input().split()))

for i in range(N):
    after[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if bfs(i, j) == 'NO':
                ans = 1
            
if ans == 1 or change > 1:
    print('NO')
else:
    print('YES')