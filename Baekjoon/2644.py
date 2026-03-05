from collections import deque

def bfs(s, e):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return visited[c] - 1
        
        for r in relation[c]:
            if not visited[r]:
                visited[r] = visited[c] + 1
                q.append(r)

    return -1

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

print(bfs(num1, num2))