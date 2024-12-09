import copy
from collections import deque

def cheese_cnt():
    cnt = 0
    for i in range(M):
        cnt += cheese[i].count(1)

    return cnt

def real_cheese(temp):
    q = deque()
    q.append((0, 0))
    temp[0][0] = -1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and temp[nx][ny] == 0:
                temp[nx][ny] = -1
                q.append((nx, ny))

def melting():
    # 녹일 치즈 좌표를 저장한 뒤에 한 번에 업데이트
    melting_cheese = []
    for i in range(M):
        for j in range(N):
            if cheese[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]

                    if 0 <= nx < M and 0 <= ny < N and temp[nx][ny] == -1:
                        cnt += 1
                if cnt > 0:
                    melting_cheese.append([i, j])

    for x, y in melting_cheese:
        cheese[x][y] = 0


M, N = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(M)]
air = [] # 만나면 녹는 찐 공기
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if cheese_cnt() == 0:
    print(time)
    print(0)
    exit(0)

else:
    while True:
        prev_cnt = cheese_cnt() # 남은 치즈 개수 세기
        
        time += 1
        temp = copy.deepcopy(cheese) 

        real_cheese(temp) # 진짜 치즈를 -1로 바꾼 리스트
        melting() # 치즈 녹임 (여기서는 temp를 참고하되, 실제 리스트의 값을 업데이트)

        if cheese_cnt() == 0:
            print(time)
            print(prev_cnt)
            exit(0)