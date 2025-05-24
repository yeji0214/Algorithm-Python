N = int(input())

for _ in range(N):
    prices = []
    ans = 0

    M = int(input())
    for _ in range(M):
        price = list(map(int, input().split()))
        prices.append(price)

    k, d, a = map(int, input().split())
    for i in range(M):
        res = k * prices[i][0] - d * prices[i][1] + a * prices[i][2]
        if res > 0:
            ans += res
    print(ans)
