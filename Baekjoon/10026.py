# # 그래프, bfs
# from collections import deque

# def bfs(x, y):
#     global area

#     q = deque()
#     q.append((x,y))
#     visited[x][y] = True
#     color = arr[x][y] # 현재 색
#     area += 1

#     while q:
#         cx, cy = q.popleft()
        
#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color and not visited[nx][ny]: # 인덱스가 범위를 벗어나지 않았고, 현재 색과 동일한 색이며, 아직 방문하지 않은 곳일 떄
#                 visited[nx][ny] = True
#                 q.append((nx, ny))


# N = int(input())
# arr = [[] * N for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
# ans = []
# area = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     arr[i] = list(input())

# # 일반 사람이 보는 경우
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             bfs(i, j)

# ans.append(area)
# area = 0
# visited = [[False] * N for _ in range(N)]

# # G -> R로 변경
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'G':
#             arr[i][j] = 'R'
            
# # 적록색약인 사람이 보는 경우
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             bfs(i, j)

# ans.append(area)

# print(*ans)

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        current_color = color[cx][cy]

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < N and color[nx][ny] == current_color and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

N = int(input())
color = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = 0
ans_arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    color[i] = list(input())

# 적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            ans += 1

ans_arr.append(ans)

# 적록색약인 사람

# G -> R로 변경
for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            ans += 1

ans_arr.append(ans)

print(*ans_arr)