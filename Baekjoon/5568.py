from itertools import permutations

n = int(input())
k = int(input())
nums = []
ans = []

for i in range(n):
    nums.append(input())

comb = list(map(list, (permutations(nums, k))))
for i in comb:
    ans.append(int(''.join(i)))

print(len(set(ans)))