# 그래프, bfs
from collections import deque

def bfs(x, y):
    global our_power, enemy_power
    power = 1
    visited[x][y] = True
    q = deque()

    current = arr[x][y] # 현재 병사 (B or W)
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N: # 범위를 벗어난 경우
                continue

            if current == arr[nx][ny] and not visited[nx][ny]: # 같은 편의 병사 + 방문하지 않은 경우
                power += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    if current == 'W': # 우리 병사
        our_power += pow(power, 2)
    else: # 적국 병사
        enemy_power += pow(power, 2)


N, M = map(int, input().split()) # 가로 크기, 세로 크기
arr = [[] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(M):
    arr[i] = list(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

our_power = 0 # 우리 병사의 위력
enemy_power = 0 # 적국 병사의 위력

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

print(our_power, enemy_power)