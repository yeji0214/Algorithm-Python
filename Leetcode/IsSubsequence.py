class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        for T in t:
            if T == s[0]:
                if len(s) > 1:
                    s = s[1:]
                else:
                    return True
        if len(s) == 0:
            return True
        return False