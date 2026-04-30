class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 1, n

        while s <= e:
            mid = (s + e) // 2

            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                e = mid - 1
            else:
                s = mid + 1