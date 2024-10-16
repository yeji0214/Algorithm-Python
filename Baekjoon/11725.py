from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        c = q.popleft()

        for t in tree[c]:
            if parent[t] == 0:
                parent[t] = c
                q.append(t)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

bfs(1)
print(*parent[2:], sep='\n')