class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current = 0
        res = []

        for n in nums:
            current += n
            res.append(current)

        return res