# bfs
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        cc = q.popleft()
        visited[cc] = True

        for i in computer[cc]:
            if not visited[i]: # 아직 방문하지 않은 컴퓨터인 경우
                q.append(i)

N = int(input())
num = int(input())
computer = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for i in range(num):
    c1, c2 = map(int, input().split())
    computer[c1].append(c2)
    computer[c2].append(c1)

bfs(1)

print(visited.count(True) - 1)



# dfs
def dfs(s):
    visited[s] = True

    for i in computer[s]:
        if not visited[i]:
            dfs(i)

N = int(input())
num = int(input())
computer = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for i in range(num):
    c1, c2 = map(int, input().split())
    computer[c1].append(c2)
    computer[c2].append(c1)

dfs(1)

print(visited.count(True) - 1)