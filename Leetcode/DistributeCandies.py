class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = set(candyType)
        eat = len(candyType) // 2

        if eat < len(candy):
            return eat
        else:
            return len(candy)