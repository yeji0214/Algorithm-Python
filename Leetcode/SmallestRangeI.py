class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 or min(nums) == max(nums):
            return 0

        def getResult(mid):
            result = []

            for n in nums:
                if abs(n - mid) <= abs(k):
                    result.append(mid)
                elif n < mid:
                    result.append(n + abs(k))
                else:
                    result.append(n - abs(k))

            return result


        s, e = min(nums), max(nums)
        ans = float('inf')

        while s <= e:
            mid = (s + e) // 2
            result = getResult(mid)

            if max(result) - min(result) < ans:
                ans = max(result) - min(result)
                s = mid + 1
            else:
                e = mid - 1

            if ans == 0:
                return 0

        return ans