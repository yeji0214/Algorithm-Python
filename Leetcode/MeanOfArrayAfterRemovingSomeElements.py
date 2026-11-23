class Solution:
    def trimMean(self, arr: list[int]) -> float:
        remove = int(0.05 * len(arr))
        arr.sort()

        for _ in range(remove):
            arr.pop(0)
            arr.pop()

        return sum(arr) / len(arr)