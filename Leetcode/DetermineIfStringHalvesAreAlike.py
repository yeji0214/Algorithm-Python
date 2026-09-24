class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()
        mid = len(s) // 2
        a, b = s[:mid], s[mid:]
        a_cnt, b_cnt = 0, 0

        for A in a:
            if A in vowel:
                a_cnt += 1

        for B in b:
            if B in vowel:
                b_cnt += 1

        if a_cnt == b_cnt:
            return True
        return False