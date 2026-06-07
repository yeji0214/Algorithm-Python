class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False

        res = {}

        for i in range(len(pattern)):
            if pattern[i] not in res:
                if words[i] in res.values():
                    return False
                res[pattern[i]] = words[i]
            elif pattern[i] in res and res[pattern[i]] != words[i]:
                return False

        return True