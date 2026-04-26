class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for S in s:
            if S == '(' or S == '[' or S == '{':
                stack.append(S)
            else:
                if stack and stack[-1] == pair[S]:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False
        return True