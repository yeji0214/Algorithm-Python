N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
direction = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]] # 동, 서, 북, 남
dice = [0, 0, 0, 0, 0, 0] # 아래, 위, 동, 서, 남, 북

for m in move:
    nx, ny = x + direction[m][0], y + direction[m][1]

    if 0 <= nx < N and 0 <= ny < M:

        if m == 1: # 동
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
        elif m == 2: # 서
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
        elif m == 3: # 북
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        else: # 남
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]

        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[0]
        else:
            dice[0] = arr[nx][ny]
            arr[nx][ny] = 0

        x, y = nx, ny
        print(dice[1])