from collections import deque

def bfs(x, y):
    count = 0
    house_map[x][y] = 0

    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        count += 1

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1:
                house_map[nx][ny] = 0
                q.append((nx, ny))

    return houses.append(count)

N = int(input())
house_map = [[] * N for _ in range(N)]
houses = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    house_map[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if house_map[i][j] == 1:
            bfs(i, j)

print(len(houses))
print(*sorted(houses), sep='\n')