class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones.sort(reverse=True)

        while len(stones) > 1:
            y = stones.pop(0)
            x = stones.pop(0)

            if x < y:
                stones.append(y - x)
                stones.sort(reverse=True)

        if stones:
            return stones[0]
        return 0