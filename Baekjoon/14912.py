n, d = map(int, input().split())
nums = [str(num) for num in range(1, n + 1)]
d = str(d)
ans = 0

for num in nums:
    ans += num.count(d)

print(ans)