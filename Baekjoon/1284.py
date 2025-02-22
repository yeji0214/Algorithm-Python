while True:
    N = input()
    if N == '0':
        exit(0)
    ans = 0
    
    for n in N:
        if n == '1':
            ans += 2
        elif n == '0':
            ans += 4
        else:
            ans += 3

    ans += len(N) + 1
    print(ans)