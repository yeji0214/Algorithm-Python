class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        dict_num = {}

        for i in range(1, 10):
            if num % i == 0:
                dict_num[i] = True
            else:
                dict_num[i] = False

        num = str(num)
        for n in num:
            ans += dict_num[int(n)]

        return ans