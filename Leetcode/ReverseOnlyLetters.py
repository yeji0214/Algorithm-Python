class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = []
        letters = []

        for S in s:
            if 'a' <= S.lower() <= 'z':
                letters.append(S)
                result.append('')
            else:
                result.append(S)

        for i in range(len(result)):
            if result[i] == '':
                result[i] = letters.pop()

        return ''.join(result)