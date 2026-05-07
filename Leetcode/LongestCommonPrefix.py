class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            prefix += strs[0][i]

            for s in strs:
                if len(s) < len(prefix) or s.find(prefix) != 0:
                    return prefix[0:-1]
                    
        return prefix