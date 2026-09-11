class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        right = [0]
        ans = []

        current_left = 0
        current_right = 0
        for i in range(1, len(nums)):
            current_left += nums[i - 1]
            current_right += nums[-i]

            left.append(current_left)
            right.append(current_right)

        right = right[::-1]

        for i in range(len(nums)):
            ans.append(abs(left[i] - right[i]))

        return ans