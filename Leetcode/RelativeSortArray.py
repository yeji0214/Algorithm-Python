class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = {}
        ans = []
        
        for a in arr1:
            cnt[a] = cnt.get(a, 0) + 1

        for a in arr2:
            for _ in range(cnt[a]):
                ans.append(a)
            del cnt[a]

        cnt = dict(sorted(cnt.items(), key=lambda x: x[0]))
        for c in cnt:
            for _ in range(cnt[c]):
                ans.append(c)

        return anss