class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []

        res = []
        for n in set(nums1):
            if n not in nums2:
                res.append(n)
        ans.append(res)

        res = []
        for n in set(nums2):
            if n not in nums1:
                res.append(n)
        ans.append(res)

        return ans