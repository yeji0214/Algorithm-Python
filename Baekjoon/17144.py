R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

purifier = []

for i in range(R):
    if arr[i][0] == -1:
        purifier.append([i, 0])
        purifier.append([i + 1, 0])
        break

for _ in range(T):
    dust = []
    res = [[0] * C for _ in range(R)]

    for px, py in purifier:
        res[px][py] = -1

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust.append([i, j])

    for dx, dy in dust:
        cnt = 0
        n_dust = arr[dx][dy] // 5
        for nx, ny in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nnx, nny = dx + nx, dy + ny
            if 0 <= nnx < R and 0 <= nny < C and arr[nnx][nny] != -1:
                res[nnx][nny] += n_dust
                cnt += 1
        res[dx][dy] += arr[dx][dy] - n_dust * cnt

    for i in range(R):
        for j in range(C):
            arr[i][j] = res[i][j]

    # 공기청정기 가동
    # 위쪽 공기청정기
    top_direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    current_d = 0
    x, y = purifier[0][0], purifier[0][1]
    cx, cy = x - 2, y
    nx, ny = x - 1, y
    
    while current_d < 4:
        if arr[cx][cy] == -1:
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = arr[cx][cy]
        nx, ny = cx, cy
        cx, cy = cx + top_direction[current_d][0], cy + top_direction[current_d][1]
        if cx < 0 or cx > x or cy < 0 or cy >= C:
            current_d += 1
            if current_d < 4:
                cx, cy = nx + top_direction[current_d][0], ny + top_direction[current_d][1]

    # 아래쪽 공기청정기
    bottom_direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    current_d = 0
    x, y = purifier[1][0], purifier[1][1]
    cx, cy = x + 2, y
    nx, ny = x + 1, y
    
    while current_d < 4:
        if arr[cx][cy] == -1:
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = arr[cx][cy]
        nx, ny = cx, cy
        cx, cy = cx + bottom_direction[current_d][0], cy + bottom_direction[current_d][1]
        if cx < x or cx >= R or cy < 0 or cy >= C:
            current_d += 1
            if current_d < 4:
                cx, cy = nx + bottom_direction[current_d][0], ny + bottom_direction[current_d][1]

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)