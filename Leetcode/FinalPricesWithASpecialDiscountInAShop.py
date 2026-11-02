class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = []

        for i in range(len(prices)):
            discount = False
            current = prices[i]
            for j in range(i + 1, len(prices)):
                if current >= prices[j]:
                    discount = True
                    ans.append(current - prices[j])
                    break
            if not discount:
                ans.append(current)

        return ans