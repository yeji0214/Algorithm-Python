class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = {}
        res2 = {}
        res = []

        for n in nums1:
            res1[n] = res1.get(n, 0) + 1
        
        for n in nums2:
            res2[n] = res2.get(n, 0) + 1

        for r in res1:
            if r in res2:
                cnt = min(res1[r], res2[r])
                for _ in range(cnt):
                    res.append(r) 

        return res