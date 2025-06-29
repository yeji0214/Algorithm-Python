L, P = map(int, input().split())
ans = L * P
participants = list(map(int, input().split()))
res = []

for p in participants:
    res.append(p - ans)

print(*res)