def dfs(s, e, ans):
    if s == e:
        return ans
    visited[s] = True
    for i in range(len(node[s])):
        next_node = node[s][i]
        if not visited[next_node]:
            distance_result = dfs(next_node, e, ans + distance[s][i])
            if distance_result is not None:
                return distance_result
    return None

N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
distance = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2, d = map(int, input().split())
    node[n1].append(n2)
    node[n2].append(n1)
    distance[n1].append(d)
    distance[n2].append(d)

for _ in range(M):
    n1, n2 = map(int, input().split())
    visited = [False] * (N + 1)
    result = dfs(n1, n2, 0)
    print(result)
