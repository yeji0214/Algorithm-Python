class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            res = [n for n in nums if n >= i]
            if len(res) == i:
                return i
        return -1