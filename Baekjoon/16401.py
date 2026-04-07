M, N = map(int, input().split())
snacks = list(map(int, input().split()))

s, e = 1, max(snacks)
ans = 0

while s <= e:
    cnt = 0
    cut = (s + e) // 2
    
    for snack in snacks:
        cnt += snack // cut

    if cnt >= M:
        s = cut + 1
        ans = cut
    else:
        e = cut - 1

print(ans)