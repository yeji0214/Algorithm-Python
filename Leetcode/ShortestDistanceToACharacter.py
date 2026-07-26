class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []

        idx = s.index(c)
        for i in range(len(s)):
            if s[i] == c:
                result.append(0)
                idx = i
            else:
                result.append(abs(i - idx))

        idx = len(s) - s[::-1].index(c) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                idx = i
            result[i] = min(result[i], abs(i - idx))

        return result