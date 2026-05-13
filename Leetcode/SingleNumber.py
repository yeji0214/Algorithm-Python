class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        sorted_cnt = list(sorted(cnt.items(), key = lambda x: x[1]))
        
        return sorted_cnt[0][0]