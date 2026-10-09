class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        l = len(arr)
        ans = 0

        for i in range(1, l + 1, 2):
            for j in range(l - i + 1):
                ans += sum(arr[j:j + i])

        return ans