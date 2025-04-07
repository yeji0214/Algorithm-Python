n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    nums = sorted(nums)

    print(f"Scenario #{i + 1}:")
    if pow(nums[0], 2) + pow(nums[1], 2) == pow(nums[2], 2):
        print("yes")
    else:
        print("no")
    print()