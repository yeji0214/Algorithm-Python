class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            ok = True
            for n in str(i):
                if int(n) == 0 or i % int(n) != 0:
                    ok = False
                    break
            if ok:
                ans.append(i)

        return ans