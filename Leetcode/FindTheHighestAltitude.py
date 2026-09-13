class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]

        current = 0
        for g in gain:
            current += g
            res.append(current)

        return max(res)