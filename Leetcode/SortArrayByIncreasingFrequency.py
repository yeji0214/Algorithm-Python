class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        frequency = {}
        ans = []

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        frequency = dict(sorted(frequency.items(), key = lambda x: (x[1], -x[0])))

        for f in frequency:
            for _ in range(frequency[f]):
                ans.append(f)

        return ans