# from collections import deque

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))

#     while q:
#         cx, cy = q.popleft()

#         for i in range(4):
#             nx, ny = cx + dx[i], cy + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:             
#                 maze[nx][ny] = maze[cx][cy] + 1

#                 if nx == N - 1 and ny == M - 1:
#                     return maze[N-1][M-1]  
                
#                 q.append((nx, ny))


# N, M = map(int, input().split())
# maze = [[] * M for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     maze[i] = list(map(int, input()))

# print(bfs(0, 0))

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1: # 이동할 수 있는 칸
                maze[nx][ny] = maze[cx][cy] + 1
                q.append((nx, ny))

    return maze[N - 1][M - 1]

N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    maze[i] = list(map(int, input()))

print(bfs(0, 0))