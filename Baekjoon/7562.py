# # 그래프, bfs
# from collections import deque

# def bfs(x, y, ex, ey):
#     q = deque()
#     q.append((x, y))

#     while q:
#         cx, cy = q.popleft()

#         if cx == ex and cy == ey:
#             return chess[cx][cy]

#         for i in range(8):
#             nx, ny = cx + dx[i], cy + dy[i]

#             if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
#                 chess[nx][ny] += chess[cx][cy] + 1
#                 q.append((nx, ny))


# T = int(input())

# dx = [-1, -2, -2, -1, 1, 2, 2, 1]
# dy = [-2, -1, 1, 2, 2, 1, -1, -2]

# for _ in range(T):
#     l = int(input())
#     chess = [[0] * l for _ in range(l)]

#     sx, sy = map(int, input().split())
#     ex, ey = map(int, input().split())

#     print(bfs(sx, sy, ex, ey)) # 현재 좌표, 목적지 좌표

from collections import deque

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        cx, cy = q.popleft()

        if cx == ex and cy == ey:
            return chess[cx][cy]
        
        for k in range(8):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                chess[nx][ny] = chess[cx][cy] + 1
                q.append((nx, ny))

T = int(input())

dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, 2, 1, -2, -1]

for _ in range(T):
    I = int(input())
    chess = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(bfs(sx, sy, ex, ey))