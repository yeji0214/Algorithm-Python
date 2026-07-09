class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = {}
        ans = 0
        set_nums = list(sorted(set(nums)))
        nums.sort()

        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        for i in range(len(set_nums) - 1):
            if set_nums[i + 1] - set_nums[i] == 1:
                ans = max(ans, cnt[set_nums[i]] + cnt[set_nums[i + 1]])

        return ans