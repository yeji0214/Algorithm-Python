from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        comb = list(map(list, combinations(arr, 3)))
        ans = 0

        for com in comb:
            int1, int2, int3 = com[0], com[1], com[2]

            if abs(int1 - int2) <= a and abs(int2 - int3) <= b and abs(int1 - int3) <= c:
                ans += 1

        return ans