def prime(n):
    for j in range(2, n):
        if n % j == 0:
            return 0
    return 1

N = int(input())
nums = list(map(int, input().split()))
ans = 0

for n in nums:
    if n > 1:
        ans += prime(n)

print(ans)