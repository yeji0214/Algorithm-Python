T = int(input())

for _ in range(T):
    N = int(input())
    res = 0

    for _ in range(N):
        data = list(map(int, input().split()))
        if max(data) > 0:
            res += max(data)

    print(res)