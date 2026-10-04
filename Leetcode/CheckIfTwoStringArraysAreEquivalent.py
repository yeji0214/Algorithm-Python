class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        res1, res2 = ''.join(word1), ''.join(word2)

        if res1 == res2:
            return True
        return False