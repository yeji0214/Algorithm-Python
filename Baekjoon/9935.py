# # 자료구조, 문자열, 스택
# string = input()
# explosion = input()
# ans = []
# last_char = explosion[-1]

# for i in string:
#     ans.append(i)
#     if i == last_char and ''.join(ans[-len(explosion):]) == explosion:
#         del ans[-len(explosion):]

# if len(ans) == 0:
#     print("FRULA")
# else:
#     print(''.join(ans))

###

S = input()
E = input()
l = E[-1]
stack = []

for s in S:
    stack.append(s)
    if l == s and ''.join(stack[-len(E):]) == E:
        del stack[-len(E):]

if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')