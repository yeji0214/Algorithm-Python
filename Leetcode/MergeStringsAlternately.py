class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_l = len(word1)
        w2_l = len(word2)
        ans = ''
        idx = min(w1_l, w2_l)

        for i in range(idx):
            ans += word1[i]
            ans += word2[i]

        if len(word1) > idx:
            ans += word1[idx:]
        elif len(word2) > idx:
            ans += word2[idx:]

        return ans