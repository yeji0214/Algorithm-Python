N, num1, num2 = map(int, input().split())
round = 1

while True:
    if abs(num1 - num2) == 1 and min(num1, num2) % 2 == 1:
        print(round)
        exit(0)
    num1 = num1 // 2 + num1 % 2
    num2 = num2 // 2 + num2 % 2
    round += 1