class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = []
        cnt2 = []
        res = []

        for n in nums1:
            if n not in cnt1:
                cnt1.append(n)

        for n in nums2:
            if n not in cnt2:
                cnt2.append(n)

        for c in cnt1:
            if c in cnt2:
                res.append(c)

        return res