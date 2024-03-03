# 그리디, 정렬, 투 포인터
N, K = map(int, input().split())

cats = sorted(map(int, input().split()))
ans = 0

s = 0
e = N-1

while e-s > 0:
    if cats[s] + cats[e] > K: # 무게 초과
        e -= 1
    else:
        ans += 1
        s += 1
        e -= 1

print(ans)