N, M = map(int, input().split())
guitar = list(map(int, input().split()))
s, e = max(guitar), sum(guitar)
ans = 0

while s <= e:
    total = 0 # 블루레이의 개수
    current = 0 # 현재 강의 길이의 합
    mid = (s + e) // 2

    for g in guitar:
        if current + g > mid:
            total += 1
            current = 0
        current += g

    if current > 0:
        total += 1

    if total > M: # 강의 길이를 늘려야 함
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)