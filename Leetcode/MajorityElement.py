class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        return sorted(cnt.items(), key = lambda x: -x[1])[0][0]