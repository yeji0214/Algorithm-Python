class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        ans = 0

        for S in s:
            if S == 'L':
                if stack and stack[-1] == 'R':
                    stack.pop()
                    if not stack:
                        ans += 1
                else:
                    stack.append(S)
            else:
                if stack and stack[-1] == 'L':
                    stack.pop()
                    if not stack:
                        ans += 1
                else:
                    stack.append(S)

        return ans