class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        isOdd = []

        for a in arr:
            if a % 2 == 1:
                isOdd.append(True)
            else:
                isOdd.append(False)

        for i in range(len(arr) - 2):
            if isOdd[i:i+3].count(True) == 3:
                return True
        return False