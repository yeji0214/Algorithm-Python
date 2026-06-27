class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for n in nums1:
            idx = nums2.index(n)
            
            if idx == len(nums2) - 1:
                ans.append(-1)
            else:
                next = [num for num in nums2[idx + 1:] if num > n]
                if len(next) == 0:
                    ans.append(-1)
                else:
                    ans.append(next[0])

        return ans