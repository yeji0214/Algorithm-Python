from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for c in combinations(cards, 3):
    if sum(c) < M:
        ans = max(ans, sum(c))
    elif sum(c) == M:
        print(M)
        exit(0)

print(ans)