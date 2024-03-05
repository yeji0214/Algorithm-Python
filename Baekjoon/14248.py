# 그래프, dfs
def dfs(s):
    if s > 0 and s <= n and not visited[s]:
        visited[s] = True
        dfs(s-stones[s-1])
        dfs(s+stones[s-1])

n = int(input())
stones = list(map(int, input().split()))
s = int(input())
visited = [False] * (n+1)

dfs(s)

print(visited.count(True))