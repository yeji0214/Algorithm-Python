class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = 100000
        ans = -100000

        for n in nums:
            current = abs(n)
            if current < closest:
                closest = current
                ans = n
            elif current == closest and ans < n:
                ans = n

        return ans