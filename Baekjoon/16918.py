from collections import deque

def explode():
    q = deque()
    for p in bomb_position:
        q.append((p[0], p[1]))

    while q:
        cx, cy = q.popleft()
        explosion[cx][cy] = '.'

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < R and 0 <= ny < C:
                explosion[nx][ny] = '.'

R, C, N = map(int, input().split())
arr = [['.'] * C for _ in range(R)]
bomb = [['O'] * C for _ in range(R)]
explosion = [['O'] * C for _ in range(R)]
bomb_position = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    arr[i] = list(input())

if N == 1:
    for a in arr:
        print(''.join(a))
    exit(0)
elif N % 2 == 0:
    for b in bomb:
        print(''.join(b))
    exit(0)

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bomb_position.append([i, j])

for i in range(2, N + 1):
    if i % 2 == 1: # 폭탄 터뜨리기
        explode()
        if i < N:
            bomb_position = []
            for x in range(R):
                for y in range(C):
                    if explosion[x][y] == 'O':
                        bomb_position.append([x, y])
            explosion = [['O'] * C for _ in range(R)]

for e in explosion:
    print(''.join(e))