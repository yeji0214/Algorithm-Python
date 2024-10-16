# 이진 탐색
N = int(input())
budget = list(map(int, input().split()))
M = int(input())

s, e = 0, max(budget)

while s <= e:
    total = 0
    mid = (s + e) // 2

    for i in budget:
        if i >= mid:
            total += mid
        else:
            total += i

    if total > M:
        e = mid - 1
    else:
        s = mid + 1

print(e)