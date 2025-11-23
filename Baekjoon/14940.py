# # 그래프, bfs
# # 주의할 점: 0(갈 수 없는 땅)이 중첩되어 있을수도 있음. 처음부터 다 돌면서 0인 경우 ans도 0으로 설정해주는 과정이 필요함.
# from collections import deque

# def bfs(x, y):
#     q = deque()
#     q.append((x,y))

#     while q:
#         cx, cy = q.popleft()

#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < n and 0 <= ny < m and ans[nx][ny] == -1: # 범위를 벗어나지 않고, 방문하지 않은 경우
#                 if land[nx][ny] == 1: # 이동할 수 있는 땅인 경우
#                     ans[nx][ny] = ans[cx][cy] + 1 # 이전 값에 +1
#                     q.append((nx, ny))

# n, m = map(int, input().split())
# land = [[] * m for _ in range(n)]
# ans = [[-1] * m for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(n):
#     land[i] = list(map(int, input().split()))

# for i in range(n):
#     for j in range(m):
#         if land[i][j] == 0:
#             ans[i][j] = 0
#         elif land[i][j] == 2:
#             # 목표 지점 좌표
#             targetX = i
#             targetY = j

# ans[targetX][targetY] = 0
# bfs(targetX, targetY)

# for i in range(len(ans)):
#     print(*ans[i])


from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                result[nx][ny] = result[cx][cy] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
si = 0
sj = 0

for i in range(n):
    lst = list(map(int, input().split()))
    if 2 in lst:
        si, sj = i, lst.index(2)
    arr[i] = lst

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(si, sj)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            result[i][j] = -1

for r in result:
    print(*r)