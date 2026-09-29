class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = bin(n)[2:]
        prev = res[0]

        for i in range(1, len(res)):
            if prev == res[i]:
                return False
            prev = res[i]

        return True