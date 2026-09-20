class Solution:
    def sortSentence(self, s: str) -> str:
        arr_words = []
        words = s.split()
        ans = []

        for w in words:
            arr_words.append([w[:-1], int(w[-1])])

        result = sorted(arr_words, key=lambda x: x[1])

        for r in result:
            ans.append(r[0])

        return ' '.join(ans)