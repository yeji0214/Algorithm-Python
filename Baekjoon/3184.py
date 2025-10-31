from collections import deque

def bfs(i, j):
    global sheep, wolf

    q = deque()
    q.append((i,  j))
    visited[i][j] = True

    s = w = 0
    if arr[i][j] == 'o':
        s += 1
    else:
        w += 1

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != '#' and not visited[nx][ny]:
                if arr[nx][ny] == 'o':
                    s += 1
                elif arr[nx][ny] == 'v':
                    w += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    if s > w:
        sheep += s
    else:
        wolf += w

R, C = map(int, input().split())
arr = [[''] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

sheep = 0
wolf = 0

for i in range(R):
    arr[i] = list(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if (arr[i][j] == 'v' or arr[i][j] == 'o') and not visited[i][j]:
            bfs(i, j)

print(sheep, wolf)

# 양 또는 늑대를 만나면 bfs 현재 좌표에서 시작
# 벽을 만나기 전이나 영역 밖으로 벗어나기 전까지 검사
# 현재 영역의 늑대의 수와 양의 수 각각 저장
# 양의 수가 늑대의 수보다 많은 경우 양의 개수만 카운트
# 아니라면 늑대의 수만 카운트
# 이미 방문한 곳은 재방문 X