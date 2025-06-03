nums = []
num_count = {}

for _ in range(10):
    num = int(input())
    nums.append(num)

    if num in num_count.keys():
        num_count[num] += 1
    else:
        num_count[num] = 1

print(sum(nums) // 10)
ans = list(k for k, v in num_count.items() if max(num_count.values()) == v)
print(ans[0])