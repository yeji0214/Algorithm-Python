N = int(input())
F = int(input())

for i in range(100):
    if i < 10:
        new = '0' + str(i)
    else:
        new = str(i)

    new_N = str(N)[:-2] + new

    if int(new_N) % F == 0:
        print(new)
        exit(0)