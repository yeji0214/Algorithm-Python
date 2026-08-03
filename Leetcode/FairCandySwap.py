class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        goal = (alice + sum(bobSizes)) // 2

        for c in aliceSizes:
            find = goal - (alice - c)
            if find in bobSizes:
                return [c, find]