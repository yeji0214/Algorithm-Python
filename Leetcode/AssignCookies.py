class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
            
        g, s = sorted(g), sorted(s)
        ans = 0

        for G in g:
            if len(s) == 0:
                break
            if s[-1] < G:
                continue
            for i in range(len(s)):
                if s[i] >= G:
                    s.pop(i)
                    ans += 1
                    break

        return ans