def clean(x, y, d):
    while True:
        dirty = 0
        if room[x][y] == 0:
            room[x][y] = 2
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= N and 0 < ny <= M and room[nx][ny] == 0:
                dirty += 1
        if dirty > 0:
            d -= 1
            if d < 0:
                d = 3
            nx = x + dx[d]
            ny = y + dy[d]

            if room[nx][ny] == 0:
                x, y = nx, ny

        else:
            nd = d + 2
            if nd > 3:
                nd %= 4

            nx = x + dx[nd]
            ny = y + dy[nd]

            if room[nx][ny] != 1:
                x, y = nx, ny
            else:
                return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
x, y = r, c
ans = 0

room = [[0] * M for _ in range(N)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    room[i] = list(map(int, input().split()))

clean(r, c, d)

for i in range(N):
    ans += room[i].count(2)

print(ans)