class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        for i in range(1, len(s)):
            result = s[i:] + s[:i]
            
            if result == goal:
                return True
        return False