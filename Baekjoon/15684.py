# 내 풀이
from itertools import combinations
import copy

def move():
    for i in range(1, N + 1):
        ci = i
        for j in range(1, H + 1):
            ci = ladder[ci][j]
        if ci != i:
            return False
    return True


N, M, H = map(int, input().split())

ladder = [[]] # 각 사다리별 이동하게 될 사다리 번호
for n in range(1, N + 1):
    ladder.append([n]* (H + 1))

lines = [list(map(int, input().split())) for _ in range(M)] # 현재 가로선들

for i, j in lines:
    ladder[j][i] = j + 1
    ladder[j + 1][i] = j

if M == 0 or move():
    print(0)
    exit(0)

candidate_lines = []

for i in range(1, H + 1):
    for j in range(1, N):
        candidate_lines.append([i, j])

for i, j in lines:
    for nj in (0, 1, -1):
        if [i, j + nj] in candidate_lines:
            candidate_lines.remove([i, j + nj])

for c in range(1, 4):
    new_lines = [list(comb) for comb in combinations(candidate_lines, c)]

    for current_lines in new_lines:
        for i, j in current_lines:
            if (i, j - 1) in current_lines or (i, j + 1) in current_lines:
                break

        for i, j in current_lines:
            lines.append([i, j])

        for i, j in current_lines:
            ladder[j][i] = j + 1
            ladder[j + 1][i] = j

        if (move()):
            print(c)
            exit(0)

        for i, j in current_lines:
            lines.remove([i, j])

        for i, j in current_lines:
            ladder[j][i] = j
            ladder[j + 1][i] = j + 1

print(-1)


# 다른 풀이

def check():
    for j in range(1, N + 1):
        cj = j
        for i in range(1, H + 1):
            if arr[i][cj] == 1:
                cj += 1
            elif arr[i][cj - 1] == 1:
                cj -= 1
        if cj != j:
            return 0
    return 1

def dfs(n, s):
    global ans

    if ans == 1:
        return
    
    if n == cnt:
        if check() == 1:
            ans = 1
        return
    
    for j in range(s, CNT):
        ti, tj = pos[j]
        if arr[ti][tj - 1] == 0 and arr[ti][tj + 1] == 0:
            arr[ti][tj] = 1
            dfs(n + 1, j + 1)
            arr[ti][tj] = 0

N, M, H = map(int, input().split())

arr = [[0] * (N + 2) for _ in range(H + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1

pos = []
for i in range(1, H + 1):
    for j in range(1, N + 1):
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i][j + 1] == 0:
            pos.append((i, j))
CNT = len(pos)

for cnt in range(4):
    ans = 0
    dfs(0, 0)
    if ans == 1:
        ans = cnt
        break
else:
    ans = -1
print(ans)