class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = {}
        ans = []
        sorted_score = sorted(score, reverse=True)

        result[sorted_score[0]] = "Gold Medal"
        if len(score) == 1:
            return ["Gold Medal"]
        result[sorted_score[1]] = "Silver Medal"
        if len(score) == 2:
            for s in score:
                ans.append(result[s])
            return ans
        result[sorted_score[2]] = "Bronze Medal"
        if len(score) == 3:
            for s in score:
                ans.append(result[s])
            return ans

        for i in range(3, len(sorted_score)):
            result[sorted_score[i]] = str(i + 1)

        for s in score:
            ans.append(result[s])
        return ans