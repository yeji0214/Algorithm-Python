class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}

        for a in arr:
            cnt[a] = cnt.get(a, 0) + 1

        result = cnt.values()
        
        if len(result) != len(set(cnt.values())):
            return False
        return True