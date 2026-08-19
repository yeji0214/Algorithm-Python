class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1), 0, -1):
            s = str1[:i]
            if str1.count(s) * len(s) == len(str1) and str2.count(s) * len(s) == len(str2):
                return s
        
        return ''
