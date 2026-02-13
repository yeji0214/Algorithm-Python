nums = [[0] * 9 for _ in range(9)]
for i in range(9):
    nums[i] = list(map(int, input().split()))
x = y = 0
max_num = 0

for i in range(9):
    c = max(nums[i])
    if c > max_num:
        max_num = c
        x = i
        y = nums[i].index(c)

print(max_num)
print(x + 1, y + 1)