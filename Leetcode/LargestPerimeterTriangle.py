class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)

        for i in range(len(nums) - 2):
            if sorted_nums[i] < sorted_nums[i + 1] + sorted_nums[i + 2]:
                return sum(sorted_nums[i:i+3])
        return 0