class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        ans[0] = 1
        total = 1
        candy = 2
        idx = 1
        candies -= 1

        while candies > 0:
            if candies < candy:
                ans[idx] += candies
                return ans
            ans[idx] += candy
            idx = (idx + 1) % num_people
            candies -= candy
            candy += 1
            total += candy

        return ans