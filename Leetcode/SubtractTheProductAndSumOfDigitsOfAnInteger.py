class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1 = 1
        n2 = 0

        n = str(n)

        for N in n:
            n1 *= int(N)
            n2 += int(N)

        return n1 - n2