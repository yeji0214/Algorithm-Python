class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        location = {}

        for i in range(len(s)):
            if s[i] in vowels:
                location[i] = s[i]

        reversed_vowels = list(location.values())[::-1]

        s = list(s)

        for l in location:
            s[l] = reversed_vowels.pop(0)

        return ''.join(s)