from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, stamp):
    q = deque()
    q.append(s)
    visited[s] = stamp
    cnt = 1

    while q:
        c = q.popleft()

        for com in computer[c]:
            if visited[com] != stamp:
                visited[com] = stamp
                cnt += 1
                q.append(com)

    return cnt

N, M = map(int, input().split())
computer = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    computer[B].append(A)

visited = [0] * (N + 1)
ans = []
max_h = 0
stamp = 0

for i in range(1, N + 1):
    stamp += 1
    res = bfs(i, stamp)
    if res == max_h:
        ans.append(i)
    elif res > max_h:
        max_h = res
        ans = [i]

print(*sorted(ans))