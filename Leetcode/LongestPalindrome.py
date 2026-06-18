class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = 0

        for S in s:
            count[S] = count.get(S, 0) + 1

        for c in count:
            ans += (count[c] // 2) * 2

        v = count.values()
        
        for V in v:
            if V % 2 == 1:
                ans += 1
                return ans

        return ans