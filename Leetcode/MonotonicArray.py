class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t = ''

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if t == 'increase':
                    return False
                t = 'decrease'
            elif nums[i] < nums[i + 1]:
                if t == 'decrease':
                    return False
                t = 'increase'

        return True
