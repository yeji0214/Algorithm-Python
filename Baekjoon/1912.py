# DP
n = int(input())
nums = list(map(int, input().split()))
result = [nums[0]]

for i in range(1, n):
    result.append(max(nums[i], result[i - 1] + nums[i]))

print(max(result))