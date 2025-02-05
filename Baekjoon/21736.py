from collections import deque

def start(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    friend = 0

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if campas[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif campas[nx][ny] == 'P' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    friend += 1

    return friend

N, M = map(int, input().split())
campas = [[] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    campas[i] = list(input())

for i in range(N):
    for j in range(M):
        if campas[i][j] == 'I':
            ans = start(i, j)
            if ans == 0:
                print('TT')
            else:
                print(ans)
            exit(0)