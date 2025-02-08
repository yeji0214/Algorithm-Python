N = list(map(int, input()))
ans = 0
M = N

while True:
    if len(M) == 1:
        N.insert(0, 0)
    s = list(map(int, str(sum(M))))
    if M == N and ans > 0:
        print(ans)
        break
    M = [M[1], s[-1]]
    ans += 1