class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            cur = s[:i]
            p = True
            for j in range(i, len(s), i):
                if cur != s[j:j+i]:
                    p = False
            if p:
                return True
        return False