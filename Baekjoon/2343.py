N, M = map(int, input().split())
guitar = list(map(int, input().split()))
s, e = max(guitar), sum(guitar)
ans = 0

while s <= e:
    total = 0 # 블루레이의 개수
    mid = (s+e) // 2
    result = 0
    for i in guitar:
        if result + i > mid:
            total += 1
            result = 0
        result += i

    if result:
        total += 1

    if total > M:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)