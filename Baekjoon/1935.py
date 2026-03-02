N = int(input())
ex = input()
operand = {}
c = 'A'

for _ in range(N):
    operand[c] = int(input())
    c = chr(ord(c) + 1)

expression = []
for e in ex:
    if e in operand:
        expression.append(operand[e])
    else:
        expression.append(e)

while len(expression) > 1:
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*', '/']:
            if i == len(expression) - 1:
                expression = expression[0:i - 2] + [f'({str(expression[i - 2])}{expression[i]}{str(expression[i - 1])})']
                break
            else:
                expression = expression[0:i - 2] + [f'({str(expression[i - 2])}{expression[i]}{str(expression[i - 1])})'] + expression[i + 1:]
                break

print(f'{eval(expression[0]):.2f}')