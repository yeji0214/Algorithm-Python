class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        dict_idx = {'type': 0, 'color': 1, 'name': 2}
        idx = dict_idx[ruleKey]
        ans = 0

        for item in items:
            if item[idx] == ruleValue:
                ans += 1

        return ans