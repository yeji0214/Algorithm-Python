class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        elif idx == len(word) - 1:
            return word[::-1]
        return word[0:idx + 1][::-1] + word[idx + 1:]