n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
res = []
num = 1
c = sequence[0]

while sequence:
    if len(stack) == 0 or stack[-1] < c:
        stack.append(num)
        res.append('+')
        num += 1

    elif stack[-1] > c:
        print("NO")
        exit(0)

    elif stack[-1] == c:
        stack.pop(-1)
        res.append('-')
        sequence.pop(0)
        if sequence:
            c = sequence[0]

print('\n'.join(res))