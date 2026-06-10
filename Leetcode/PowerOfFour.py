class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        nums = []
        for i in range(17):
            nums.append(4 ** i)

        if n in nums:
            return True
        return False