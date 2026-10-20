# def solution(s):
#     stack = []
    
#     for S in s:
#         if S == '(':
#             stack.append('(')
#         else:
#             if len(stack) == 0:
#                 return False
#             stack.pop()
            
#     if len(stack) > 0:
#         return False

#     return True


def solution(s):
    stack = []

    for S in s:
        if S == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True

print(solution("(()("))