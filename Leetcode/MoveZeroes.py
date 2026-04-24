class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0

        for n in nums:
            if n != 0:
                nums[idx] = n
                idx += 1

        for i in range(idx, len(nums)):
            nums[i] = 0