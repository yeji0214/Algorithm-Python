X = int(input())
stick = [64]

while True:
    if sum(stick) == X:
        print(len(stick))
        exit(0)
    if sum(stick) > X:
        num = stick.pop(-1) // 2
        stick.append(num)
        stick.append(num)

        if sum(stick[:-1]) >= X:
            stick.pop(-1)