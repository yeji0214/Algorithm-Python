# # 그래프, bfs
# from collections import deque

# def bfs(location):
#     q = deque()

#     for l in location:
#         q.append((l[0], l[1]))

#     while q:
#         cx, cy = q.popleft()

#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
#                 tomato[nx][ny] = tomato[cx][cy] + 1
#                 q.append((nx, ny))

# M, N = map(int, input().split())
# tomato = [[] * M for _ in range(N)]
# location = []
# unripe = 0 # 안 익은 토마토
# ans = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     tomato[i] = list(map(int, input().split()))
#     unripe += tomato[i].count(0)

# if unripe == 0: # 안 익은 토마토가 없는 경우 (모든 토마토가 익어있는 상태)
#     ans = 1

# else:
#     unripe = 0

#     for i in range(N):
#         for j in range(M):
#             if tomato[i][j] == 1:
#                 location.append([i, j])

#     bfs(location)

#     for i in range(N):
#         unripe += tomato[i].count(0)
#         ans = max(ans, max(tomato[i]))

#     if unripe > 0: # 안 익은 토마토가 있다! (토마토가 모두 익지는 못하는 상황)
#         ans = 0

# print(ans - 1)

###

from collections import deque

def bfs(ripen):
    global ans

    q = deque()
    for r in ripen:
        q.append((r[0], r[1]))

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[cx][cy] + 1
                q.append((nx, ny))


M, N = map(int, input().split())
tomato = [[0] * M for _ in range(N)]
ripen = []
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tomato[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripen.append([i, j])

bfs(ripen)

for i in range(N):
    if 0 in tomato[i]:
        print(-1)
        exit(0)
    ans = max(ans, max(tomato[i]))

print(ans - 1)