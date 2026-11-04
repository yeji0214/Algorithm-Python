class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            drink, remain = numBottles // numExchange, numBottles % numExchange
            ans += drink

            numBottles = drink + remain

        return ans