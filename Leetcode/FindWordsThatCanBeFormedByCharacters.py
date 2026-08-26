class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        ans = 0

        for c in chars:
            dic[c] = dic.get(c, 0) + 1

        for word in words:
            p = True
            word_dic = {}
            for w in word:
                word_dic[w] = word_dic.get(w, 0) + 1
            for wd in word_dic:
                if wd not in dic or dic[wd] < word_dic[wd]:
                    p = False
            if p:
                ans += len(word)

        return ans