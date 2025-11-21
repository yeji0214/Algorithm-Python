# from collections import deque

# def bfs():
#     q = deque()
#     for p in start:
#         q.append(p)

#     while q:
#         cx, cy = q.popleft()

#         for i in range(4):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == '0' and not visited[nx][ny]:
#                 q.append((nx, ny))
#                 visited[nx][ny] = True

# M, N = map(int, input().split())
# arr = [[] * N for _ in range(M)]
# visited = [[False] * N for _ in range(M)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# for i in range(M):
#     arr[i] = list(input())

# start = []

# for i in range(N):
#     if arr[0][i] == '0':
#         start.append((0, i))
#         visited[0][i] = True

# bfs()

# for i in range(N):
#     if visited[M - 1][i]:
#         print('YES')
#         exit(0)

# print('NO')


from collections import deque

def bfs():
    q = deque()
    for e in electric:
        q.append(e)

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))

M, N = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
electric = []

for i in range(M):
    arr[i] = list(map(int, input()))

for i in range(N):
    if arr[0][i] == 0:
        electric.append((0, i))
        visited[0][i] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()

for i in range(N):
    if visited[M-1][i]:
        print("YES")
        exit(0)
print("NO")