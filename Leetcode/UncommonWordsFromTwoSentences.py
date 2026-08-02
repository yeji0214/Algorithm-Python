class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        s1_result = {}
        s2_result = {}
        ans = []

        for s in s1_words:
            s1_result[s] = s1_result.get(s, 0) + 1
        for s in s2_words:
            s2_result[s] = s2_result.get(s, 0) + 1

        for s in s1_result:
            if s1_result[s] == 1 and s not in s2_result:
                ans.append(s)

        for s in s2_result:
            if s2_result[s] == 1 and s not in s1_result:
                ans.append(s)

        return ans