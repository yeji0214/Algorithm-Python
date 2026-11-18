class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0

        for S in s:
            if S == '(':
                stack.append('(')
                ans = max(ans, len(stack))
            elif S == ')':
                stack.pop()

        return ans