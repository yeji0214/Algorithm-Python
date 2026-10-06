class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []

        for n in nums:
            ans.append(nums[n])

        return ans