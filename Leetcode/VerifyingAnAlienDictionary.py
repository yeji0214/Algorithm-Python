class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        dict_a = {}
        a = ord('a')
        dict_res = []

        for i in range(26):
            c = chr(a + i)
            dict_a[c] = order.index(c)

        for word in words:
            r = []
            for w in word:
                r.append(dict_a[w])
            dict_res.append([word, r])

        res = sorted(dict_res, key=lambda x: x[1])
        ans = []

        for r in res:
            ans.append(r[0])

        if words == ans:
            return True
        return False