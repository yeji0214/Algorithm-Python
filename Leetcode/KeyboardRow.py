class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []

        for w in words:
            idx = 0
            no = False
            for i in range(len(rows)):
                if w[0].lower() in rows[i]:
                    idx = i
            for i in range(1, len(w)):
                if w[i].lower() not in rows[idx]:
                    no = True
                    break
            if not no:
                ans.append(w)
        
        return ans
                