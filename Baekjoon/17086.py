from collections import deque

def bfs():
    q = deque()
    for i, j in shark:
        q.append((i, j))
        visited[i][j] = True

    while q:
        cx, cy = q.popleft()

        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                arr[nx][ny] = arr[cx][cy] + 1
                q.append((nx, ny))
                visited[nx][ny] = True


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
shark = []
ans = 0

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append([i, j])

bfs()

for a in arr:
    ans = max(ans, max(a))

print(ans - 1)