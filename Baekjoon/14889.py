# 내 풀이
from itertools import combinations

N = int(input())
S = [[0] * N for _ in range(N)]
all_team = list(i for i in range(N))
ans = 101

for i in range(N):
    S[i] = list(map(int, input().split()))

teams = list(map(list, (combinations(all_team, N // 2))))

for t in teams:
    t1 = t
    t2 = list(set(all_team) - set(t1))
    t1_sum = 0
    t2_sum = 0

    for i in combinations(t1, 2):
        t1_sum += (S[i[0]][i[1]] + S[i[1]][i[0]])

    for i in combinations(t2, 2):
        t2_sum += (S[i[0]][i[1]] + S[i[1]][i[0]])

    ans = min(ans, abs(t1_sum - t2_sum))

print(ans)


# 백트래킹
N = int(input())
M = N // 2
S = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9

def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            a_sum, b_sum = 0, 0
            for i in range(M):
                for j in range(M):
                    a_sum += S[alst[i]][alst[j]]
                    b_sum += S[blst[i]][blst[j]]
            ans = min(ans, abs(a_sum - b_sum))
        return

    dfs(n + 1, alst + [n], blst)
    dfs(n + 1, alst, blst + [n])

dfs(0, [], [])
print(ans)