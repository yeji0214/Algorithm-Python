class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                possible = 1
            if n <= possible:
                return True
            return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if flowerbed[i + 1] == 0:
                    possible += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    possible += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                    possible += 1
                    flowerbed[i] = 1

        if n <= possible:
            return True
        return False