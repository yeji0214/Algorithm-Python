# # 그래프, bfs
# from itertools import combinations
# from collections import deque
# import copy

# def bfs():
#     cnt = 0
#     q = deque()
#     for j in virus:
#         q.append((j[0], j[1]))

#     while q:
#         cx, cy = q.popleft()

#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 q.append((nx, ny))

#     for a in range(N):
#         cnt += temp[a].count(0)

#     return cnt


# N, M = map(int, input().split())
# arr = [[]*M for _ in range(N)]
# wall = []
# virus = []
# ans = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     arr[i] = list(map(int, input().split()))

# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             wall.append([i, j])
#         elif arr[i][j] == 2:
#             virus.append([i, j])

# wall_list = list(combinations(wall, 3))

# for i in wall_list:
#     temp = copy.deepcopy(arr)
#     temp[i[0][0]][i[0][1]] = 1
#     temp[i[1][0]][i[1][1]] = 1
#     temp[i[2][0]][i[2][1]] = 1

#     ans = max(ans, bfs())

# print(ans)

from itertools import combinations
from collections import deque
import copy

def bfs():
    q = deque()
    
    for v in virus:
        q.append((v[0], v[1]))

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0

    for i in range(N):
        cnt += temp[i].count(0)

    return cnt


N, M = map(int, input().split())
lab = [[0] *  M for _ in range(N)]

wall = []
virus = []
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    lab[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            wall.append([i, j])
        elif lab[i][j] == 2:
            virus.append([i, j])

wall_list = list(combinations(wall, 3))

for w in wall_list:
    temp = copy.deepcopy(lab)
    temp[w[0][0]][w[0][1]] = 1
    temp[w[1][0]][w[1][1]] = 1
    temp[w[2][0]][w[2][1]] = 1

    ans = max(ans, bfs())

print(ans)