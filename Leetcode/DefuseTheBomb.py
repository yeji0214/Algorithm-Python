class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        arr = code * 2
        ans = []
        l = len(code)

        if k > 0:
            for i in range(l):
                ans.append(sum(arr[i + 1:i + k + 1]))
        elif k == 0:
            return [0] * l
        else:
            for i in range(l):
                ans.append(sum(arr[i + l + k:i + l]))

        return ans