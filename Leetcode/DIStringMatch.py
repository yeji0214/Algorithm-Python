class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        numbers = [i for i in range(0, len(s) + 1)]
        result = []

        for S in s:
            if S == 'I':
                result.append(numbers.pop(0))
            else:
                result.append(numbers.pop())
        result.append(numbers.pop())

        return result