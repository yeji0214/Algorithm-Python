class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = 0

        for i in range(len(nums)):
            if i == 0:
                right = sum(nums[i + 1:])
            elif i == len(nums) - 1:
                left = sum(nums[:i])
                right = 0
            else:
                left += nums[i - 1]
                right -= nums[i]

            if left == right:
                return i
        return -1