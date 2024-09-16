# bfs
from collections import deque

def bfs(z, x, y):
    q = deque()
    q.append((z, x, y))

    while q:
        cz, cx, cy = q.popleft()

        for i in range(6):
            nz, nx, ny = cz + dz[i], cx + dx[i], cy + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = 1
                    if building[nz][nx][ny] == '.':
                        building[nz][nx][ny] = building[cz][cx][cy] + 1
                        q.append((nz, nx, ny))

                    elif building[nz][nx][ny] == 'E':
                        return building[cz][cx][cy] + 1
            
    return 0


# 동서남북상하
dx = [0, 0, 1, -1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        exit(0)

    building = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            b = input()
            building[i][j] = list(b)
            if 'S' in b:
                z, x, y = i, j, b.index('S')
        input()

    building[z][x][y] = 0
    visited[z][x][y] = 1

    ans = bfs(z, x, y)

    if ans == 0: # 시작 위치 넘겨줌
        print("Trapped!")
    else:
        print("Escaped in " + str(ans) + " minute(s).")