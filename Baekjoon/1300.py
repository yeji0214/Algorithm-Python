# 이진 탐색
# 댕어렵다
N = int(input())
k = int(input())
s, e = 1, N * N
ans = 0

while s <= e:
    total = 0
    mid = (s + e) // 2

    for i in range(1, N + 1):
        total += min(mid // i, N)

    if total >= k:
        e = mid - 1
    else:
        s = mid + 1

    ans = s

print(ans)