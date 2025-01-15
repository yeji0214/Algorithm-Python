stick = input()
stack = []
ans = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if stick[i - 1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)