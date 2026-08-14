class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        goal = sum(arr) // 3
        ok = 0
        current = 0

        for a in arr:
            current += a
            if current == goal:
                current = 0
                ok += 1

        if ok >= 3:
            return True
        return False