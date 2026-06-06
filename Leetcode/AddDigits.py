class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            lst = list(map(int, str(num)))
            num = sum(lst)
        return num