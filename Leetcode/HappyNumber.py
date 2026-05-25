class Solution:
    def isHappy(self, n: int) -> bool:
        appear = []

        while True:
            if n == 1:
                return True
            n = str(n)
            nxt = 0
            for N in n:
                int_n = int(N)
                nxt += (int_n * int_n)
            if nxt in appear:
                return False
            appear.append(nxt)
            n = nxt