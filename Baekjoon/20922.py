N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
ans = 0
s = 0

for e in range(N):
    dic[A[e]] = dic.get(A[e], 0) + 1
    
    while dic[A[e]] > K:
        dic[A[s]] -= 1
        s += 1

    ans = max(ans, e - s + 1)

print(ans)