class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        ans = 0

        for i in range(m):
            arr = [s[i] for s in strs]
            if arr != sorted(arr):
                ans += 1

        return ans