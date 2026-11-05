import copy

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        ans = list(copy.deepcopy(s))

        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return ''.join(ans)