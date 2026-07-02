class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result = [word.upper(), word.lower(), word[0].upper() + word[1:].lower()]

        if word in result:
            return True
        return False