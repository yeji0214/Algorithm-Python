N = int(input())
F = [['N'] * N for _ in range(N)]
ans = 0

for i in range(N):
    F[i] = list(input())

for i in range(N):
    friends = set()
    for j in range(N):
        if F[i][j] == 'Y':
            friends.add(j)

            for k in range(N):
                if F[j][k] == 'Y':
                    friends.add(k)
    friends.discard(i)
    ans = max(ans, len(friends))

print(ans)