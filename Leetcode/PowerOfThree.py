class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        nums = []

        for i in range(21):
            nums.append(3 ** i)

        if n in nums:
            return True
        return False