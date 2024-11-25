N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N - 1, 0), (N - 1, 1), (N-2, 0), (N-2, 1)]
direction = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(M):
    d, s = map(int, input().split())
    n_cloud = []

    for x, y in cloud:
        nx, ny = x + direction[d][0] * s, y + direction[d][1] * s
        if nx < 0: nx = N - (-nx % N)
        if nx >= N: nx = nx % N
        if ny < 0: ny = N - (-ny % N)
        if ny >= N: ny = ny % N
        n_cloud.append((nx, ny))

    cloud = n_cloud
    
    for x, y in cloud:
        arr[x][y] += 1

    # 물복사버그 마법
    for x, y in cloud:
        cnt = 0
        for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
                cnt += 1
        arr[x][y] += cnt

    n_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in cloud:
                n_cloud.append((i, j))
                arr[i][j] -= 2
    cloud = n_cloud

ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)