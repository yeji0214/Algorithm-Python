class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(set(nums))
        exist = []

        for i in range(len(nums)):
            if nums[i] in exist:
                nums[i] = 101
            else:
                exist.append(nums[i])

        nums.sort()
    
        return res