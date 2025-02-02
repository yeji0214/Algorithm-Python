S1, S2, S3 = map(int, input().split())
nums = {}
d1 = [i for i in range(1, S1 + 1)]
d2 = [i for i in range(1, S2 + 1)]
d3 = [i for i in range(1, S3 + 1)]

for i in d1:
    for j in d2:
        for k in d3:
            num = i + j + k
            if num in nums.keys():
                nums[num] += 1
            else:
                nums[num] = 1

ans = min([key for key, value in nums.items() if value == max(nums.values())])

print(ans)