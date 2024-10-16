from itertools import combinations, permutations

N = int(input())

ability = [[0] * N for _ in range(N)]
ans = 1e9

for i in range(N):
    ability[i] = list(map(int, input().split()))

team = list(i for i in range(0, N))
team1 = list(map(list, combinations(team, N // 2)))

for t1 in team1:
    t1_res = 0
    t2_res = 0

    t2 = list(set(team) - set(t1))

    # 각 팀에서 모든 조합의 능력을 더해야 함
    # 그리고 두 팀의 차이를 구해!

    t1_a = list(map(list, permutations(t1, 2)))
    t2_a = list(map(list, permutations(t2, 2)))

    for a in t1_a:
        t1_res += ability[a[0]][a[1]]

    for a in t2_a:
        t2_res += ability[a[0]][a[1]]

    ans = min(ans, abs(t1_res - t2_res))

print(ans)