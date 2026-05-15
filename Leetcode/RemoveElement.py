class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
            else:
                cnt += 1
        nums.sort()

        return cnt