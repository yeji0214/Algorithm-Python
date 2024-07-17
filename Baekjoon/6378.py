N = 1

def digital_root():
    while True:
        N = list(map(int, input()))
        ans = 0
        if N[0] == 0:
            return
        elif len(N) == 1:
            print(N[0])
        else:
            while len(N) > 1:
                ans = str(sum(N))
                N = list(map(int, ans))
            print(ans)

digital_root()