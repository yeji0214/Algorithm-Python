class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = 10001

        for i in range(1, len(prices)):
            buy_price = min(buy_price, prices[i - 1])
            res = max(res, prices[i] - buy_price)

        return res