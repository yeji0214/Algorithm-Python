class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = {}
        cnt2 = {}

        for r in ransomNote:
            cnt1[r] = cnt1.get(r, 0) + 1

        for m in magazine:
            cnt2[m] = cnt2.get(m, 0) + 1

        for c in cnt1:
            if c not in cnt2 or cnt2[c] < cnt1[c]:
                return False
        return True