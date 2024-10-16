# 브루트포스
from itertools import combinations
from collections import deque
import copy

def surrounding(x, y):
    village = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and planet[nx][ny] == 1:
            village += 1
        
    return village

def bfs(p1, p2):
    ans = 0

    q = deque()
    q.append(p1)
    q.append(p2)

    while q:
        cp = q.popleft()
        village = 0
        
        for i in range(4):
            nx, ny = cp[0] + dx[i], cp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] >= 0:
                temp[nx][ny] = temp[cp[0]][cp[1]] - 1
                q.append([nx, ny])

        for i in range(N):
            village += temp[i].count(1)

        if village == 0:
            for i in range(N):
                ans = min(ans, min(temp[i]))
            return ans


N, M = map(int, input().split())
planet = [[] * M for _ in range(N)]
empty = []
times = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(N):
    planet[i] = list(map(int, input()))

for i in range(N):
    for j in range(M):
        if planet[i][j] == 0 and surrounding(i, j) > 0:
            empty.append([i, j])

poison = map(list, combinations(empty, 2))
for p in poison:
    temp = copy.deepcopy(planet)
    temp[p[0][0]][p[0][1]] = -1
    temp[p[1][0]][p[1][1]] = -1
    times.append(bfs(p[0], p[1]))

print(abs(max(times)) - 1)