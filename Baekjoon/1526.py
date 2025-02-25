N = int(input())

while True:
    no = 0
    for n in str(N):
        if n != '4' and n != '7':
            no = 1
            break
    if no == 0:
        print(N)
        exit(0)
    N -= 1