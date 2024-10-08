from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
ans = 0

a = list(map(list,permutations(A, N)))

for i in range(len(a)):
    res = 0
    for j in range(N - 1):
        res += abs(a[i][j] - a[i][j + 1])
    ans = max(ans, res)

print(ans)