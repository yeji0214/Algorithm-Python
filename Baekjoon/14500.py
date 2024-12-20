N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

tetromino = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (-1, 2)], [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)], [(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (0, 1), (-1, 1), (1, 1)], [(0, 0), (0, 1), (0, 2), (-1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(0, 0), (0, 1), (-1, 1), (-2, 1)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (-1, 0), (-2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 1), (1, 2)], [(0, 0), (-1, 0), (-1, 1), (-2, 1)], [(0, 0), (0, 1), (1, 0), (2, 0)]]

for i in range(N):
    for j in range(M):
        for t in range(len(tetromino)):
            no = 0
            res = 0
            for x, y in tetromino[t]:
                ni, nj = i + x, j + y
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    no = 1
                    break
                else:
                    res += arr[ni][nj]
            if no == 0:
                ans = max(ans, res)

print(ans)