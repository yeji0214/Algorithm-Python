class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        num = int(''.join(digits))

        return list(map(int, str(num + 1)))