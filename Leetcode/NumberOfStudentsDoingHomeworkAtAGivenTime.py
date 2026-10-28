class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        ans = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1

        return ans