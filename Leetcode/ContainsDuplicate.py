class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}

        for n in nums:
            if n in res:
                return True
            else:
                res[n] = 0

        return False