class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        split_s = s.split()

        for S in split_s:
            words.append(S[::-1])

        return ' '.join(words)