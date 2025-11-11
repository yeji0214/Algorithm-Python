# # 그래프, bfs
# from collections import deque

# def bfs(x, y):
#     global total_painting
#     current_area = 0

#     visited[x][y] = True
#     q = deque()

#     if arr[x][y] == 1:
#         q.append((x,y))
#         total_painting += 1
#         current_area = 1

#     while q:
#         cx, cy = q.popleft()

#         for k in range(4):
#             nx = cx + dx[k]
#             ny = cy + dy[k]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:  # 범위를 벗어님
#                 continue
#             visited[nx][ny] = True
#             if arr[nx][ny] == 1:
#                 q.append((nx, ny))
#                 current_area += 1

#     return current_area

# n, m = map(int, input().split())
# arr = [[] * m for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# total_painting = 0
# broadest_painting = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# for i in range(n):
#     arr[i] = list(map(int, input().split()))

# for i in range(n):
#     for j in range(m):
#         if not visited[i][j]: # 방문하지 않은 곳
#             broadest_painting = max(broadest_painting, bfs(i, j))

# print(total_painting)
# print(broadest_painting)


from collections import deque

def bfs(i ,j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    current_area = 1

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                current_area += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    return current_area

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
area = 0

for i in range(n):
    arr[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = max(area, bfs(i, j))

print(cnt)
print(area)