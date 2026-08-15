class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        parentheses = []
        result = ''
        ans = []

        for S in s:
            result += S
            if S == '(':
                stack.append(S)
            else:
                stack.pop()
                if not stack:
                    parentheses.append(result)
                    result = ''

        for p in parentheses:
            ans.append(p[1:-1])
            
        return ''.join(ans)