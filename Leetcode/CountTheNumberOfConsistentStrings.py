class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0

        for word in words:
            p = True
            for w in word:
                if w not in allowed:
                    p = False
                    break
            if p:
                ans += 1

        return ans