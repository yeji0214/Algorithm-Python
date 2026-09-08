from itertools import combinations

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        com = list(combinations(nums, 2))
        ans = 0

        for c in com:
            if c[0] == c[1]:
                ans += 1

        return ans