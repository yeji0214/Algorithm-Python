N, C = map(int, input().split())
home = sorted([int(input()) for _ in range(N)])
s, e = 1, home[-1] - home[0]
ans = 0

while s <= e:
    mid = (s + e) // 2
    total = 1 # 설치 가능한 공유기의 개수
    current = home[0]

    for h in range(1, len(home)):
        if home[h] >= current + mid:
            total += 1
            current = home[h]

    if total >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)