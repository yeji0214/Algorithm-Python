A, B, C, M = map(int, input().split())
ans = 0
fatigue = 0

for i in range(24):
    if fatigue + A > M:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0
    else:
        ans += B
        fatigue += A

print(ans)