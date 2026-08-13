class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        while k > 0:
            if nums[0] < 0:
                nums[0] = -nums[0]
                k -= 1
                nums.sort()
            else:
                if k % 2 == 0:
                    k = 0
                else:
                    nums[0] = -nums[0]
                    k = 0
                    nums.sort()

        return sum(nums)