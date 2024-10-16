# bfs
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        
        if cx == N - 1 and cy == M - 1: # 목적지 도착
            return maze[cx][cy]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[cx][cy] + 1
                q.append((nx, ny))


N, M = map(int, input().split())
maze = [[]* M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    maze[i] = list(map(int, input()))

print(bfs(0, 0))