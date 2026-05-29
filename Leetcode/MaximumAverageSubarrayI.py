class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        ans = current / k

        for i in range(0, len(nums) - k):
            current -= nums[i]
            current += nums[i + k]
            ans = max(ans, current / k)

        return ans