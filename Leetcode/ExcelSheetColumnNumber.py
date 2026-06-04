class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ord_a = ord('A')
        l = len(columnTitle)

        if l == 1:
            return ord(columnTitle) - ord_a + 1

        ans = 0
        num = 26
        mul = 1

        ans += ord(columnTitle[-1]) - ord_a + 1

        for i in range(2, l + 1):
            ans += (num ** mul) * (ord(columnTitle[l-i]) - ord_a + 1)
            mul += 1

        return ans