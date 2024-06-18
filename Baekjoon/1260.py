from collections import deque

def dfs(n):
    visited[n] = True
    print(n, end=' ')

    for i in nums[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        c = q.popleft()

        visited[c] = True
        print(c, end=' ')
        
        for i in nums[c]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

N, M, V = map(int, input().split())
nums = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    n1, n2 = map(int, input().split())
    nums[n1].append(n2)
    nums[n2].append(n1)

for i in range(N+1):
    nums[i] = sorted(nums[i])

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)