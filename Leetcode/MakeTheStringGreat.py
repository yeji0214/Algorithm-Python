class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            remove = False
            for i in range(len(s) - 1):
                s1, s2 = s[i], s[i + 1]

                if abs(ord(s1) - ord(s2)) == 32:
                    s = s[:i] + s[i+2:]
                    remove = True
                    break
            if not remove:
                return s
        return s
            