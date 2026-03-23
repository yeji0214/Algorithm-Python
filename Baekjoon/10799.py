# stick = input()
# stack = []
# ans = 0

# for i in range(len(stick)):
#     if stick[i] == '(':
#         stack.append('(')
#     else:
#         stack.pop()
#         if stick[i - 1] == '(':
#             ans += len(stack)
#         else:
#             ans += 1

# print(ans)

S = input()
stack = []
ans = 0

for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if S[i - 1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)