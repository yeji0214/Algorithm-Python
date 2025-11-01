# from collections import deque

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True

#     while q:
#         cx, cy = q.popleft()
        
#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and water[nx][ny] > 0:
#                 visited[nx][ny] = True
#                 water[nx][ny] = -1
#                 q.append((nx, ny))


# N = int(input())
# area = [[0] * N for _ in range(N)]
# max_height = 0
# ans = 0 # 안전한 영역의 개수

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     area[i] = list(map(int, input().split()))
#     max_height = max(max_height, max(area[i]))

# for i in range(max_height + 1):
#     water = [[element - i for element in row] for row in area]  # 물에 잠기는 경우를 처리할 배열
#     visited = [[False] * N for _ in range(N)]
#     current_area = 0

#     for a in range(N):
#         for b in range(N):
#             if water[a][b] > 0:
#                 bfs(a, b)
#                 current_area += 1

#     ans = max(ans, current_area)

# print(ans)


from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not submerge[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

N = int(input())
arr = [[0] * N for _ in range(N)]
max_l = 0
ans = 0

for i in range(N):
    arr[i] = list(map(int, input().split()))
    max_l = max(max_l, max(arr[i]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(0, max_l + 1):
    submerge = [[False] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    res = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] <= i:
                submerge[x][y] = True

    for x in range(N):
        for y in range(N):
            if not submerge[x][y] and not visited[x][y]:
                bfs(x, y)
                res += 1

    ans = max(ans, res)

print(ans)