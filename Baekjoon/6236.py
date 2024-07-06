# 이진 탐색
N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
s, e = max(money), sum(money)
ans = 0

while s <= e:
    total = 0
    result = 0
    mid = (s + e) // 2

    for m in money:
        if result + m > mid:
            result = 0
            total += 1
        result += m

    if result > 0:
        total += 1

    if total > M:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)