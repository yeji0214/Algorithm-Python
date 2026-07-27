class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        sentences = sentence.split()
        result = []
        suffix = 'a'

        for s in sentences:
            if s[0].lower() in vowel:
                result.append(s + 'ma' + suffix)
            else:
                result.append(s[1:] + s[0] + 'ma' + suffix)
            suffix += 'a'

        return ' '.join(result)