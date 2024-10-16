N = int(input())

nums = [[] * N for _ in range(N)]
ans = 0

for i in range(N):
	nums[i] = list(map(int, input().split()))
	if 0 in nums[i]:
		x = i
		y = nums[i].index(0)

ans += (sum(nums[x]) + sum(row[y] for row in nums))
print(ans)