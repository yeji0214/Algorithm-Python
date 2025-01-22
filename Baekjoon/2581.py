def isPrime(n):
    if n < 2:
        return False
    for j in range(2, n // 2 + 1):
        if n % j == 0:
            return False
    return True

M = int(input())
N = int(input())
ans = []

for i in range(M, N + 1):
    if isPrime(i):
        ans.append(i)

if len(ans) == 0:
    print(-1)
    exit(0)
print(sum(ans))
print(min(ans))