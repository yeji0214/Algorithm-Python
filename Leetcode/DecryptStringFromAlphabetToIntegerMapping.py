class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt = {}
        s = s[::-1]
        ans = ''

        for i in range(1, 10):
            decrypt[i] = chr(96 + i)
        for i in range(10, 27):
            decrypt[str(i) + '#'] = chr(96 + i)

        i = 0
        while i < len(s):
            if s[i] == '#':
                ans += decrypt[str(s[i:i+3])[::-1]]
                i += 3
            else:
                ans += decrypt[int(s[i])]
                i += 1

        return ans[::-1]