class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        res = ""
        for ls in lower_s:
            if '0' <= ls <= '9' or 'a' <= ls <='z':
                res += ls

        if res == res[::-1]:
            return True
        return False