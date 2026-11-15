class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        exist = [False for _ in range(10000)]
        missing = 0

        for a in arr:
            exist[a - 1] = True

        for i in range(10000):
            if not exist[i]:
                missing += 1
            if missing == k:
                return i + 1