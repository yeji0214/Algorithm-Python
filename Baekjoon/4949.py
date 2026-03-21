# while True:
#     str = input()
#     stack = []
#     no = 0

#     if str == '.':
#         exit(0)
#     for s in str:
#         if s == '[' or s == '(':
#             stack.append(s)
#         elif s == ']':
#             if len(stack) == 0 or stack.pop() != '[':
#                 no = 1
#                 break
#         elif s == ')':
#             if len(stack) == 0 or stack.pop() != '(':
#                 no = 1
#                 break
#     if len(stack) > 0:
#         no = 1
#     if no == 1:
#         print("no")
#     else:
#         print("yes")

while True:
    S = input()
    if S == '.':
        exit(0)
    stack = []
    ans = True

    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                ans = False
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                ans = False
                break

    if len(stack) == 0 and ans:
        print("yes")
    else:
        print("no")