class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for S in s:
            if S == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(S)

        for T in t:
            if T == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(T)

        if s_stack == t_stack:
            return True
        return False