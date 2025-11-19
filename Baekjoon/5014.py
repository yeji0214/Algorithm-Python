from collections import deque

def bfs():
    q = deque()
    q.append(S)
    visited[S] = True

    while q:
        c = q.popleft()
        if c == G:
            return cnt[c]
        move = [c + U, c - D]

        for m in move:
            if 0 < m <= F and not visited[m]:
                visited[m] = True
                cnt[m] = cnt[c] + 1
                q.append(m)
    return "use the stairs"

F, S, G, U, D = map(int, input().split())
cnt = [0] * (F + 1)
visited = [False] * (F + 1)

print(bfs())