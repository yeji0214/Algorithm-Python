import sys
from collections import deque

def bfs(n, end):
    q = deque()
    q.append(n)

    while q:
        c = q.popleft()
        if c == end:
            return cnt[c]
        if 0 <= c * 2 < 100001 and not visited[c * 2]: # 순간 이동
            visited[c * 2] = True
            cnt[c * 2] = cnt[c]
            q.appendleft(c * 2) # 먼저 처리
        if 0 <= c - 1 < 100001 and not visited[c - 1]:
            visited[c - 1] = True
            cnt[c - 1] = cnt[c] + 1
            q.append(c - 1)
        if 0 <= c + 1 < 100001 and not visited[c + 1]:
            visited[c + 1] = True
            cnt[c + 1] = cnt[c] + 1
            q.append(c + 1)

N, K = map(int, sys.stdin.readline().split())
cnt = [0] * 100001
visited = [False] * 100001

print(bfs(N, K))