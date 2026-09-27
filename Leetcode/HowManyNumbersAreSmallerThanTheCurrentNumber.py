class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        ans = []

        for n in nums:
            idx = sorted_nums.index(n)
            if idx > 0:
                idx -= sorted_nums[:idx].count(n)
            ans.append(idx)

        return ans