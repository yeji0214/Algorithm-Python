class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for S in s:
            if S == '*':
                stack.pop()
            else:
                stack.append(S)

        return ''.join(stack)