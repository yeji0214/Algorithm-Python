# # 그래프, dfs
# def dfs(s):
#     if s > 0 and s <= n and not visited[s]:
#         visited[s] = True
#         dfs(s-stones[s-1])
#         dfs(s+stones[s-1])

# n = int(input())
# stones = list(map(int, input().split()))
# s = int(input())
# visited = [False] * (n+1)

# dfs(s)

# print(visited.count(True))

from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        c = q.popleft()
        move = [c - A[c], c + A[c]]

        for m in move:
            if 0 <= m < n and not visited[m]:
                visited[m] = True
                q.append(m)

n = int(input())
A = list(map(int, input().split()))
s = int(input())
visited = [False] * n

bfs(s - 1)

print(visited.count(True))