N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]
ans = 0
current = 0

for d in dice:
    ans += 1
    nxt = current + d

    if nxt >= N - 1:
        print(ans)
        exit(0)

    current = nxt + board[nxt]

    if current >= N - 1:
        print(ans)
        exit(0)

print(ans)