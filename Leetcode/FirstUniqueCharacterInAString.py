class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = {}

        for i in range(len(s)):
            if s[i] in index:
                index[s[i]].append(i)
            else:
                index[s[i]] = [i]

        for idx in index:
            if len(index[idx]) == 1:
                return index[idx][0]
        return -1