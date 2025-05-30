from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0 ,0, -1, 1, 1, -1, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        cx, cy = q.popleft()

        for k in range(8):
            nx, ny = cx + dx[k], cy + dy[k]
            
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        exit(0)

    arr = [[0] * w for _ in range(h)]

    for i in range(h):
        arr[i] = list(map(int, input().split()))

    visited = [[False] * w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i, j)
                ans += 1

    print(ans)