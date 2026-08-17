class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != new_heights[i]:
                ans += 1

        return ans