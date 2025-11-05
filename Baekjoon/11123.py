from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i ,j))
    visited[i][j] = True

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and arr[nx][ny] == '#':
                visited[nx][ny] = True
                q.append((nx, ny))

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

for _ in range(T):
    H, W = map(int, input().split())
    arr = [['.'] * W for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    ans = 0

    for i in range(H):
        arr[i] = list(input())

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                ans += 1

    print(ans)