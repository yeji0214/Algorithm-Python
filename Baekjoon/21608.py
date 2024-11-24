N = int(input())
arr = [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]
students = [list(map(int, input().split())) for _ in range(N * N)]
sorted_lst = [[0] * 5] + sorted(students)

for s in students:
    like_mx = empty_mx = -1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0: continue
            like_cnt = empty_cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if arr[ni][nj] in s:
                    like_cnt += 1
                if arr[ni][nj] == 0:
                    empty_cnt += 1

            if like_mx < like_cnt or like_mx == like_cnt and empty_mx < empty_cnt:
                like_mx, empty_mx = like_cnt, empty_cnt
                ei, ej = i, j

    arr[ei][ej] = s[0]

score = [0, 1, 10, 100, 1000]
ans = 0
for i in range(1, N + 1):
    for j in range(1, N +1):
        cnt = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if arr[ni][nj] in sorted_lst[arr[i][j]]:
                cnt += 1

        ans += score[cnt]

print(ans)