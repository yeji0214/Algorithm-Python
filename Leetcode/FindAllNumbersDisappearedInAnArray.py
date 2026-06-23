class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lst = [i for i in range(1, len(nums) + 1)]

        return list(set(lst) - set(nums))