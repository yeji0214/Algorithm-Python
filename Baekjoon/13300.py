student = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0]}

N, K = map(int, input().split())

for _ in range(N):
    S, Y = map(int, input().split())
    student[Y][S] += 1

res = []
ans = 0

for v in student.values():
    res += v

for r in res:
    if 0 < r <= K:
        ans += 1
    else:
        ans += r // K
        if r % K > 0:
            ans += 1

print(ans)