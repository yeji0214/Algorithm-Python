C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
    exit(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

grid = [[0] * C for _ in range(R)]
direction = 0
x = R - 1
y = 0

for seat in range(1, C * R + 1):
    if seat == K:
        print(y + 1, R - x)
        exit(0)

    grid[x][y] = seat
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= R or y < 0 or y >= C or grid[x][y]:
        x -= dx[direction]
        y -= dy[direction]

        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]