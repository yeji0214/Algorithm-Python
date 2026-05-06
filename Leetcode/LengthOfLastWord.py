class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")[::-1]
        
        for w in words:
            if w:
                return len(w)