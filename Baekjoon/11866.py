# 구현
# 왠지 모르게 헤맸던 문제,,

N, K = map(int, input().split())
arr = list(range(1, N+1))
res = []
index = 0

while len(arr) > 0:
    index += (K-1)
    index = index % len(arr)
    res.append(arr.pop(index))

print("<",end="")
print(*res, sep=", ", end="")
print(">")