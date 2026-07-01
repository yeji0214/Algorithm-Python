class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]

        for i in range(2, 31):
            F.append(F[i - 2] + F[i - 1])

        return F[n]