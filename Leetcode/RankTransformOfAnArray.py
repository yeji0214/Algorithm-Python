class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = sorted(list(set(arr)))
        sort_dict = {}
        res = []

        for i in range(len(sort_arr)):
            sort_dict[sort_arr[i]] = i + 1

        for a in arr:
            res.append(sort_dict[a])

        return res