class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        twice, missing = 0, 0

        for i in range(1, len(nums) + 1):
            if i in nums and nums.count(i) == 1:
                continue
            elif i not in nums:
                missing = i
            elif nums.count(i) == 2:
                twice = i
            if missing > 0 and twice > 0:
                return [twice, missing]