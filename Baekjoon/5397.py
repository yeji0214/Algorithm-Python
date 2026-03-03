T = int(input())

for _ in range(T):
    password = input()
    left = []
    right = []

    for p in password:
        if p == '<' and left:
            right.append(left.pop())
        elif p == '>' and right:
            left.append(right.pop())
        elif p == '-' and left:
            left.pop()
        elif p != '<' and p != '>' and p != '-':
            left.append(p)

    print(''.join(left + right[::-1]))