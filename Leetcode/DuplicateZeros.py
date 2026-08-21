class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        ans = []

        for a in arr:
            if a == 0:
                ans.append(0)
                ans.append(0)
            else:
                ans.append(a)

        arr[:] = ans[:len(arr)]
        