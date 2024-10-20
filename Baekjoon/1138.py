# 그리디
N = int(input())
h = list(map(int, input().split()))
p = list(range(1, N+1))
res = []

j = -1
for i in range(N):
    res.insert(h[j], p[j])
    j -= 1

print(*res)