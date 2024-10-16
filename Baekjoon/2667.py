# from collections import deque

# def bfs(x, y):
#     count = 0
#     house_map[x][y] = 0

#     q = deque()
#     q.append((x, y))

#     while q:
#         cx, cy = q.popleft()
#         count += 1

#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]

#             if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1:
#                 house_map[nx][ny] = 0
#                 q.append((nx, ny))

#     return houses.append(count)

# N = int(input())
# house_map = [[] * N for _ in range(N)]
# houses = []

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# for i in range(N):
#     house_map[i] = list(map(int, input()))

# for i in range(N):
#     for j in range(N):
#         if house_map[i][j] == 1:
#             bfs(i, j)

# print(len(houses))
# print(*sorted(houses), sep='\n')

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    house_cnt = 1

    while q:
        cx, cy = q.popleft()

        for n in range(4):
            nx, ny = cx + dx[n], cy + dy[n]

            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 1:
                q.append((nx, ny))
                house[nx][ny] = -1
                house_cnt += 1

    return house_cnt

N = int(input())
house = [[] for _ in range(N)]
ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    house[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            house[i][j] = -1
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans), sep='\n')