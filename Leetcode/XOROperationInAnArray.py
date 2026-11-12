class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        ans = 0

        for i in range(n):
            nums.append(start + 2 * i)

        for n in nums:
            ans ^= n

        return ans