from collections import deque
import copy

def taxi(temp_goorm_map, sx, sy, ex, ey):
    q = deque()
    q.append((sy-1, sx-1))
    
    while q:
        cx, cy = q.popleft()
        if cx == ey - 1 and cy == ex - 1:
            return
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and temp_goorm_map[nx][ny] == 0:
                temp_goorm_map[nx][ny] = temp_goorm_map[cx][cy] + 1
                q.append((nx, ny))

N, M = list(map(int, input().split()))
X, Y, Z = list(map(int, input().split()))
goorm_map = []
guest = []
profit = 0 # 수익
total_distance = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    goorm_map.append(list(map(int, input().split())))
    
for _ in range(M):
    guest.append(list(map(int, input().split())))
    
# 택시 시작점 - 도착점 이동 거리
for g in guest:
    x, y = g[0], g[1] # 시작점
    temp_goorm_map = copy.deepcopy(goorm_map)
    temp_goorm_map[y-1][x-1] = 1
    taxi(temp_goorm_map, x, y, g[2], g[3])
    distance = temp_goorm_map[g[3] - 1][g[2] - 1] - 1
    total_distance += distance
    if distance <= 5:
        profit += X
    else:
        profit += X + (distance - 5) * Y

# 다음 손님까지의 이동 거리
for m in range(M-1):
    sx, sy, ex, ey = guest[m][2], guest[m][3], guest[m+1][0], guest[m+1][1]
    temp_goorm_map = copy.deepcopy(goorm_map)
    taxi(temp_goorm_map, sx, sy, ex, ey)
    total_distance += temp_goorm_map[ey - 1][ex - 1]

print(profit - total_distance * Z)