from collections import deque

def bfs(mid):
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()

        if current == end:
            return True
        
        for next, limit in graph[current]:
            if not visited[next] and limit >= mid:
                visited[next] = True
                q.append(next)

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((B, C))
    graph[B].append((A, C))

start, end = map(int, input().split())

low, high = 1, 1000000000
ans = low

while low <= high:
    mid = (low + high) // 2
    if bfs(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)