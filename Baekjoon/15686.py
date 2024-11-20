def cal(lst):
    sm = 0
    for hx, hy in home:
        mn = 2*N
        for cx, cy in lst:
            mn = min(mn, abs(hx - cx) + abs(hy - cy))
        sm += mn
    return sm

def dfs(n, lst):
    global ans
    if n == CNT:
        if len(lst) == M:
            ans = min(ans, cal(lst))
        return
    
    dfs(n + 1, lst + [chicken[n]]) # 유지
    dfs(n + 1, lst) # 폐업

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
ans = 2*N*2*N

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
CNT = len(chicken)

dfs(0, [])
print(ans)