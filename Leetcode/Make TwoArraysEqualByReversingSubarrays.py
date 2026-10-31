class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        dict_target = {}
        dict_arr = {}

        for t in target:
            dict_target[t] = dict_target.get(t, 0) + 1

        for t in arr:
            dict_arr[t] = dict_arr.get(t, 0) + 1

        for t in dict_target:
            if t not in dict_arr or dict_arr[t] != dict_target[t]:
                return False
        return True