class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = []

        for n in nums:
            if n % 2 == 0:
                res.insert(0, n)
            else:
                res.append(n)

        return res