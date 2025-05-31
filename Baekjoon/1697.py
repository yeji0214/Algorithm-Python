from collections import deque

def bfs(N):
    q = deque()
    q.append(N)
    visited[N] = True

    while q:
        c = q.popleft()

        loc = [c - 1, c + 1, 2 * c]

        for l in loc:
            if 0 <= l <= 100000 and not visited[l]:
                q.append(l)
                visited[l] = True
                arr[l] = arr[c] + 1
        if c == K:
            return

N, K = map(int, input().split())

arr = [0] * 100001
visited = [False] * 100001

bfs(N)

print(arr[K])