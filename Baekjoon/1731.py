N = int(input())
nums = [int(input()) for _ in range(N)]

if (nums[1] - nums[0]) == (nums[2] - nums[1]):
    nxt = nums[1] - nums[0]
    print(nums[-1] + nxt)
    exit(0)
else:
    nxt = nums[1] // nums[0]
    print(nums[-1] * nxt)
    exit(0)