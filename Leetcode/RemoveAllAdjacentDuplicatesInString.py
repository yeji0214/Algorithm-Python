class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for S in s:
            if stack and stack[-1] == S:
                stack.pop()
            else:
                stack.append(S)

        return ''.join(stack)