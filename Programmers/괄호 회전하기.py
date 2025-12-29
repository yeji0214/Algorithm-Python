def correct(S):
    stack = []
    
    for s in S:
        if s == '[' or s == '(' or s == '{':
            stack.append(s)
        elif s == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif s == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif s == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
            
    if len(stack) > 0:
        return False
    return True

def solution(s):
    ans = 0
    
    for i in range(len(s)):
        new_str = s[i:] + s[:i]
        
        if correct(new_str):
            ans += 1
        
    return ans