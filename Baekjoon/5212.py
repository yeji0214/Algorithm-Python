from collections import deque

def bfs(land):
    q = deque()
    for l in land:
        q.append(l)
    sink = []

    while q:
        cx, cy = q.popleft()
        cnt = 0

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            # 영역을 벗어나거나 .인 경우: 바다
            if nx < 0 or nx >= R or ny < 0 or ny >= C or M[nx][ny] == '.':
                cnt += 1

        if cnt >= 3:
            sink.append([cx, cy])

    for s in sink:
        M[s[0]][s[1]] = '.'

R, C = map(int, input().split())
M = [['.'] * C for _ in range(R)]

for i in range(R):
    M[i] = list(input())

land = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if M[i][j] == 'X':
            land.append([i, j])

bfs(land)

min_r, max_r = R, -1
min_c, max_c = C, -1

for i in range(R):
    for j in range(C):
        if M[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

for i in range(min_r, max_r + 1):
    print(''.join(M[i][min_c:max_c + 1]))