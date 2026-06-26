class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0

        consecutive = 0
        for n in nums:
            if n == 0:
                ans = max(ans, consecutive)
                consecutive = 0
            else:
                consecutive += 1
        ans = max(ans, consecutive)

        return ans