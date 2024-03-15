# 그래프, bfs
from collections import deque

def bfs(x, y):
    peak = []
    q = deque()
    q.append((x,y))
    peak.append([x,y])
    current = arr[x][y] # 현재 좌표의 높이

    while q:
        cx, cy = q.popleft()

        for k in range(8):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < M and [nx, ny] not in peak: # 범위 내
                if arr[nx][ny] > current: # 현재 높이보다 높은 경우 (현재 좌표가 산봉우리가 X)
                    return 0
                elif arr[nx][ny] == current: # 현재 높이와 동일 (인접한 격자를 더 검사해서 산봉우리가 맞는지 아닌지 확인해 볼 필요 O)
                    q.append((nx, ny))
                    peak.append([nx,ny])

    for k in range(len(peak)):
        arr[peak[k][0]][peak[k][1]] = 501

    return 1 
                

N, M = map(int, input().split())
arr = [[] * M for _ in range(N)]
ans = 0
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if arr[i][j] != 501:
            ans += bfs(i, j)

print(ans)

# 이미 산봉우리가 된 좌표는 값을 바꿔주는 게 맞음 (그래야 중복 카운트가 되지 X)