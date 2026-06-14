class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        change = {}

        for i in range(len(s)):
            if s[i] not in change:
                if t[i] in change.values():
                    return False
                change[s[i]] = t[i]
            elif change[s[i]] != t[i]:
                return False

        return True