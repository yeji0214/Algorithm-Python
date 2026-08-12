class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = list(map(list, words))
        ans = []
        
        for w in words[0]:
            no = False
            for i in range(1, len(words)):
                if w not in words[i]:
                    no = True
                    break
            if not no:
                for i in range(1, len(words)):
                    words[i][words[i].index(w)] = ''
                ans.append(w)

        return ans