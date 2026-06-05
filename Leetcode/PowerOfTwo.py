class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        nums = []

        for i in range(32):
            nums.append(pow(2, i))

        if n in nums:
            return True
        return False