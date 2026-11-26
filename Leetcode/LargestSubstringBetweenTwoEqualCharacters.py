class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index = {}
        ans = 0

        for i in range(len(s)):
            if s[i] in index:
                index[s[i]].append(i)
            else:
                index[s[i]] = [i]

        if not list(i for i in index.values() if len(i) > 1):
            return -1

        for i in index.values():
            if len(i) > 1:
                ans = max(ans, i[-1] - i[0] - 1)

        return ans