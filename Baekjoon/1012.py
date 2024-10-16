from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            # 새 좌표가 범위 내에 있으면서 배추인 경우
            if 0 <= nx < M and 0 <= ny < N and cabbage[nx][ny] == 1:
                cabbage[nx][ny] = 0
                q.append((nx, ny))


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * N for _ in range(M)]
    ans = 0 # 필요한 배추흰지렁이 수

    for i in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1

    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1: # 배추 발견!
                bfs(i, j)
                ans += 1

    print(ans)