from itertools import combinations
import copy

def move():
    # for i in range(1, H + 1):
    #     # ci = i
    #     for j in range(1, N + 1):
    #         # if [ci, j] in lines:
    #         ci = ladder[j][ci]
    #     if ci != i:
    #         return False
    # return True

    for i in range(1, H):
        ci = i
        for j in range(1, N + 1):
            # ci = ladder[j][ci]
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
        # print('current: ' + str(current_lines))
    
        for i, j in current_lines:
            if (i, j - 1) in current_lines or (i, j + 1) in current_lines:
                break

        for i, j in current_lines:
            lines.append([i, j])

        original_ladder = copy.deepcopy(ladder)

        for i, j in current_lines:
            ladder[j][i] = j + 1
            ladder[j + 1][i] = j

        if (move()):
            print(c)
            exit(0)

        for i, j in current_lines:
            lines.remove([i, j])

        ladder = original_ladder

print(-1)

# ladder 업데이트부터 해야됨