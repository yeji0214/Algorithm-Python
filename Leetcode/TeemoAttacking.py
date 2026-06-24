class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        skip = False

        for i in range(len(timeSeries)):
            if not skip:
                s = timeSeries[i]
            finish = timeSeries[i] + duration - 1
            if i + 1 < len(timeSeries) and timeSeries[i + 1] <= finish:
                skip = True
            else:
                ans += finish - s + 1
                skip = False

        return ans