# 내 풀이
from collections import deque

def bfs():
    q = deque()
    q.append(list(land.keys())[0])
    integration = []
    sm = 0
    delete_keys = []

    while q:
        cx, cy = q.popleft()

        if (cx, cy) in land:
            for l in land[(cx, cy)]:
                if l not in integration:
                    nx, ny = l
                    integration.append(l)
                    sm += population[nx][ny]
                    delete_keys.append(tuple(l))
                    q.append((nx, ny))

    for key in delete_keys:
        if key in land:
            del land[key]
    
    total = sm // len(integration)
    for x, y in integration:
        population[x][y] = total


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    land = {}
    for i in range(N):
        for j in range(N):
            cp = population[i][j]
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < N and 0 <= nj < N and L <= abs(cp - population[ni][nj]) <= R:
                    if (i, j) in land.keys():
                        land[(i, j)].append([ni, nj])
                    else:
                        land[(i, j)] = [[ni, nj]]

    if len(land) == 0:
        break

    while len(land) > 0:
        bfs()
    ans += 1

print(ans)


# 다른 풀이
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))

    v[i][j] = 1
    lst = [(i, j)]
    sm = population[i][j]

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and L <= abs(population[ci][cj] - population[ni][nj]) <= R:
                q.append((ni, nj))
                v[ni][nj] = 1
                lst.append((ni, nj))
                sm += population[ni][nj]

    if len(lst) > 1:
        avg = sm // len(lst)
        for ti, tj in lst:
            population[ti][tj] = avg

        return 1
    return 0

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    v = [[0] * N for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                flag = max(flag, bfs(i, j))

    if flag == 0:
        break
    ans += 1

print(ans)