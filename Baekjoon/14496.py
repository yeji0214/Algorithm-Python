from collections import deque

def bfs(a, b):
    q = deque()
    q.append(a)

    while q:
        c = q.popleft()
        if c == b:
            return visited[c]
        
        for r in R[c]:
            if r != a and visited[r] == 0:
                visited[r] = visited[c] + 1
                q.append(r)

    return -1

a, b = input().split()
N, M = map(int, input().split())
R = {}
visited = {}

for _ in range(M):
    c1, c2 = input().split()

    if c1 in R:
        R[c1].append(c2)
    else:
        R[c1] = [c2]

    if c2 in R:
        R[c2].append(c1)
    else:
        R[c2] = [c1]

    if c1 not in visited:
        visited[c1] = 0
    if c2 not in visited:
        visited[c2] = 0

print(bfs(a, b))