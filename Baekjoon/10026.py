# 그래프, bfs
from collections import deque

def bfs(x, y):
    global area

    q = deque()
    q.append((x,y))
    visited[x][y] = True
    color = arr[x][y] # 현재 색
    area += 1

    while q:
        cx, cy = q.popleft()
        
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color and not visited[nx][ny]: # 인덱스가 범위를 벗어나지 않았고, 현재 색과 동일한 색이며, 아직 방문하지 않은 곳일 떄
                visited[nx][ny] = True
                q.append((nx, ny))


N = int(input())
arr = [[] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = []
area = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    arr[i] = list(input())

# 일반 사람이 보는 경우
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

ans.append(area)
area = 0
visited = [[False] * N for _ in range(N)]

# G -> R로 변경
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
            
# 적록색약인 사람이 보는 경우
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

ans.append(area)

print(*ans)