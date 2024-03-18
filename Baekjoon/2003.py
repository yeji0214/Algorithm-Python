# 브루트포스, 투포인터
N, M = map(int, input().split())
num = list(map(int, input().split()))
s = e = 0
ans = 0

while s <= e < N:
    if M == sum(num[s:e+1]):
        ans += 1
        s += 1
        if s > e:
            e += 1
    elif M > sum(num[s:e+1]):
        e += 1
    else:
        s += 1
        if s > e:
            e += 1

print(ans)