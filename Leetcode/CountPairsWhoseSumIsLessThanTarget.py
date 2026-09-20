from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        idx = [i for i in range(len(nums))]
        com = combinations(idx, 2)
        ans = 0

        for c in com:
            if nums[c[0]] + nums[c[1]] < target:
                ans += 1

        return ans