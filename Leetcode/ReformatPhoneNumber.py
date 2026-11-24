class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = []
        number = number.replace("-", "")
        number = number.replace(" ", "")

        while True:
            if len(number) > 4:
                nums.append(number[:3])
                number = number[3:]
            elif len(number) == 4:
                nums.append(number[:2])
                nums.append(number[2:])
                break
            else:
                nums.append(number)
                break

        return '-'.join(nums)