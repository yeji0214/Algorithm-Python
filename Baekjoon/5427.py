from collections import deque

def fire_bfs():
    q = deque()
    for f in fires:
        q.append((f[0], f[1]))
        fire_time[f[0]][f[1]] = 0

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[cx][cy] + 1
                q.append((nx, ny))

def move_bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    time[sx][sy] = 0

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                return time[cx][cy] + 1

            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.' and time[nx][ny] == 0 and (fire_time[nx][ny] == -1 or fire_time[nx][ny] > time[cx][cy] + 1):
                time[nx][ny] = time[cx][cy] + 1
                q.append((nx, ny))

    return 'IMPOSSIBLE'

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    w, h = map(int, input().split())
    building = [['#'] * w for _ in range(h)]
    time = [[0] * w for _ in range(h)]
    fire_time = [[-1] * w for _ in range(h)]
    sx = sy = 0
    fires = []

    for i in range(h):
        building[i] = list(input())
        
        if '@' in building[i]:
            sx = i
            sy = building[i].index('@')

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fires.append([i, j])

    fire_bfs()
    print(move_bfs(sx, sy))