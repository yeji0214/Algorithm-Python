class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        def uncommon(s, c, ans):
            for i in range(len(s), 0, -1):
                for j in range(0, len(s) - i + 1):
                    if s[j:j + i] not in c:
                        ans = max(ans, i)
                        return ans
            return ans

        ans = -1

        ans = uncommon(a, b, ans)
        ans = uncommon(b, a, ans)

        return ans