from collections import deque

def bfs(i, j):
    q = deque()
    q.append(i)

    while q:
        c = q.popleft()

        for f in friends[c]:
            if f == j:
                return distance[c] + 1
            if f != i and distance[f] == 0:
                distance[f] = distance[c] + 1
                q.append(f)


N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)

for i in range(1, N + 1):
    res = 0
    for j in range(1, N + 1):
        distance = [0] * (N + 1)
        if i != j:
            res += bfs(i, j)
    ans.append(res)

print(ans.index(min(ans)) + 1)